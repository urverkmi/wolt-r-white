from ..models.models import Dish, Ingredient, UserProfile
from typing import Dict, List
from ..data.placeholder import *

def predict_ingredients_for_dish(dish: Dish) -> List[Ingredient]:
    """
    In reality, you'd call an ML model here based on dish.description, etc.
    For demo, we just map ingredient_ids to Ingredient objects.
    """
    return [INGREDIENTS[i] for i in dish.ingredient_ids if i in INGREDIENTS]


def get_user_pref_dict(user: UserProfile) -> Dict[int, float]:
    if not user:
        return {}
    return {p.ingredient_id: p.weight for p in user.preferences}


def score_dish_for_user(dish: Dish, user: UserProfile) -> float:
    """
    Simple linear scoring:
      score = sum(user_weight[ingredient] for each ingredient present)
    """
    prefs = get_user_pref_dict(user)
    score = 0.0
    for ing_id in dish.ingredient_ids:
        score += prefs.get(ing_id, 0.0)
    return score

