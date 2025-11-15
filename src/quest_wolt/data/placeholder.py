from ..models.models import *

INGREDIENTS: Dict[int, Ingredient] = {
    1: Ingredient(id=1, name="onion"),
    2: Ingredient(id=2, name="garlic"),
    3: Ingredient(id=3, name="chicken"),
    4: Ingredient(id=4, name="rice"),
    5: Ingredient(id=5, name="cheese"),
}

RESTAURANTS: Dict[int, Restaurant] = {
    1: Restaurant(id=1, name="Mama's Kitchen", lat=60.1699, lon=24.9384),
    2: Restaurant(id=2, name="Spice Route", lat=60.1705, lon=24.9410),
}

DISHES: Dict[int, Dish] = {
    1: Dish(
        id=1,
        restaurant_id=1,
        name="Garlic Chicken Rice Bowl",
        description="Grilled chicken with garlic, onions and steamed rice.",
        ingredient_ids=[1, 2, 3, 4],
    ),
    2: Dish(
        id=2,
        restaurant_id=1,
        name="Cheesy Onion Soup",
        description="Onion soup topped with melted cheese.",
        ingredient_ids=[1, 5],
    ),
    3: Dish(
        id=3,
        restaurant_id=2,
        name="Spicy Garlic Noodles",
        description="Noodles with garlic and chili oil.",
        ingredient_ids=[2],
    ),
}

USERS: Dict[int, UserProfile] = {
    1: UserProfile(
        id=1,
        name="Demo User",
        preferences=[
            UserPreference(ingredient_id=1, weight=-0.8),  # hates onion
            UserPreference(ingredient_id=2, weight=0.5),   # likes garlic
            UserPreference(ingredient_id=3, weight=0.8),   # likes chicken
        ],
    )
}

QUESTS: Dict[int, Quest] = {
    1: Quest(
        id=1,
        user_id=1,
        title="Try 2 new garlic dishes",
        steps=[
            QuestStep(id=1, description="Try Garlic Chicken Rice Bowl", restaurant_id=1, dish_id=1),
            QuestStep(id=2, description="Try Spicy Garlic Noodles", restaurant_id=2, dish_id=3),
        ],
    )
}