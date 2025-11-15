from fastapi import FastAPI, HTTPException, Query
from .models.models import *
from .data.placeholder import INGREDIENTS, USERS, DISHES, RESTAURANTS, QUESTS


app = FastAPI(title="FoodQuest Demo API")


# ---------
# Helper functions (fake ML / scoring)
# ---------

def predict_ingredients_for_dish(dish: Dish) -> List[Ingredient]:
    """
    In reality, you'd call an ML model here based on dish.description, etc.
    For demo, we just map ingredient_ids to Ingredient objects.
    """
    return [INGREDIENTS[i] for i in dish.ingredient_ids if i in INGREDIENTS]


def get_user_pref_dict(user_id) -> Dict[int, float]:
    user = USERS.get(user_id)
    if not user:
        return {}
    return {p.ingredient_id: p.weight for p in user.preferences}


def score_dish_for_user(dish: Dish, user_id: int) -> float:
    """
    Simple linear scoring:
      score = sum(user_weight[ingredient] for each ingredient present)
    """
    prefs = get_user_pref_dict(user_id)
    score = 0.0
    for ing_id in dish.ingredient_ids:
        score += prefs.get(ing_id, 0.0)
    return score


# ---------
# User & Preferences
# ---------

@app.get("/users/{user_id}", response_model=UserProfile)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/users/{user_id}/preferences", response_model=List[UserPreference])
def get_user_preferences(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.preferences


@app.put("/users/{user_id}/preferences", response_model=List[UserPreference])
def update_user_preferences(user_id: int, req: UpdatePreferencesRequest):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Overwrite for demo. In reality, you'd merge / partially update.
    user.preferences = req.preferences
    USERS[user_id] = user
    return user.preferences


@app.post("/users/{user_id}/feedback/dishes")
def add_dish_feedback(user_id: int, feedback: DishFeedback):
    # For the demo, we just print or log it and maybe slightly tweak prefs.
    if feedback.dish_id not in DISHES:
        raise HTTPException(status_code=404, detail="Dish not found")

    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Very naive "learning": if rating >=4, bump up ingredients; if <=2, bump down.
    dish = DISHES[feedback.dish_id]
    delta = 0.1 if feedback.rating >= 4 else -0.1 if feedback.rating <= 2 else 0.0

    if delta != 0.0:
        pref_map = get_user_pref_dict(user_id)
        for ing_id in dish.ingredient_ids:
            old = pref_map.get(ing_id, 0.0)
            new = max(-1.0, min(1.0, old + delta))
            pref_map[ing_id] = new

        # write back to user.preferences
        user.preferences = [UserPreference(ingredient_id=k, weight=v) for k, v in pref_map.items()]
        USERS[user_id] = user

    return {"message": "Feedback recorded"}


# ---------
# Restaurants & Dishes
# ---------

@app.get("/restaurants/nearby", response_model=List[Restaurant])
def get_nearby_restaurants(
    lat: float = Query(...),
    lon: float = Query(...),
    radius_km: float = Query(5.0),
):
    # For demo, we ignore radius and just return everything.
    return list(RESTAURANTS.values())


@app.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: int):
    rest = RESTAURANTS.get(restaurant_id)
    if not rest:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return rest


@app.get("/restaurants/{restaurant_id}/dishes", response_model=List[Dish])
def get_restaurant_dishes(restaurant_id: int):
    if restaurant_id not in RESTAURANTS:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return [d for d in DISHES.values() if d.restaurant_id == restaurant_id]


@app.get("/dishes/{dish_id}", response_model=Dish)
def get_dish(dish_id: int):
    dish = DISHES.get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish


@app.post("/dishes/{dish_id}/predict-ingredients", response_model=List[Ingredient])
def predict_dish_ingredients(dish_id: int):
    dish = DISHES.get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return predict_ingredients_for_dish(dish)


# ---------
# Recommendations
# ---------

class RecommendedDish(BaseModel):
    dish: Dish
    score: float

@app.get("/users/{user_id}/recommendations", response_model=List[RecommendedDish])
def get_recommendations(
    user_id: int,
    lat: float = Query(...),
    lon: float = Query(...),
    radius_km: float = Query(5.0),
):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    # For demo: consider all dishes, score them, sort.
    scores: List[RecommendedDish] = []
    for dish in DISHES.values():
        s = score_dish_for_user(dish, user_id)
        scores.append(RecommendedDish(dish=dish, score=s))

    # Sort descending by score
    scores.sort(key=lambda x: x.score, reverse=True)
    return scores


# ---------
# Quests
# ---------

@app.get("/users/{user_id}/quests/active", response_model=Quest)
def get_active_quest(user_id: int):
    # For demo, just return the first active quest for that user
    for q in QUESTS.values():
        if q.user_id == user_id and q.status == "active":
            return q
    raise HTTPException(status_code=404, detail="No active quest for user")


@app.post("/users/{user_id}/quests", response_model=Quest)
def create_quest(user_id: int):
    global NEXT_QUEST_ID
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    # Very simple quest generation: "Try top 2 recommended dishes"
    recs = get_recommendations(user_id=user_id, lat=0, lon=0, radius_km=5.0)
    top_recs = recs[:2]

    steps = []
    step_id = 1
    for r in top_recs:
        rest_id = r.dish.restaurant_id
        rest = RESTAURANTS[rest_id]
        desc = f"Try {r.dish.name} at {rest.name}"
        steps.append(
            QuestStep(
                id=step_id,
                description=desc,
                restaurant_id=rest_id,
                dish_id=r.dish.id,
            )
        )
        step_id += 1

    quest = Quest(
        id=NEXT_QUEST_ID,
        user_id=user_id,
        title="Explore new dishes nearby",
        steps=steps,
    )
    QUESTS[quest.id] = quest
    NEXT_QUEST_ID += 1
    return quest


@app.patch("/users/{user_id}/quests/{quest_id}", response_model=Quest)
def update_quest(user_id: int, quest_id: int, req: UpdateQuestRequest):
    quest = QUESTS.get(quest_id)
    if not quest or quest.user_id != user_id:
        raise HTTPException(status_code=404, detail="Quest not found")

    # Update a single step status
    if req.step_id is not None and req.status is not None:
        for step in quest.steps:
            if step.id == req.step_id:
                step.status = req.status

        # If all steps completed, mark quest completed
        if all(s.status == "completed" for s in quest.steps):
            quest.status = "completed"

    # Optionally allow updating entire quest status
    if req.step_id is None and req.status is not None:
        quest.status = req.status

    QUESTS[quest_id] = quest
    return quest