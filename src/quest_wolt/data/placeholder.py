from ..models.models import *
from typing import Dict

# -----------------
# Ingredients
# -----------------

INGREDIENTS: Dict[int, Ingredient] = {
    1: Ingredient(id=1, name="onion"),
    2: Ingredient(id=2, name="garlic"),
    3: Ingredient(id=3, name="chicken"),
    4: Ingredient(id=4, name="rice"),
    5: Ingredient(id=5, name="cheese"),
    6: Ingredient(id=6, name="tomato"),
    7: Ingredient(id=7, name="basil"),
    8: Ingredient(id=8, name="chili"),
    9: Ingredient(id=9, name="cream"),
    10: Ingredient(id=10, name="mushroom"),
    11: Ingredient(id=11, name="noodles"),
    12: Ingredient(id=12, name="beef"),
    13: Ingredient(id=13, name="pork"),
    14: Ingredient(id=14, name="tofu"),
    15: Ingredient(id=15, name="shrimp"),
    16: Ingredient(id=16, name="salmon"),
    17: Ingredient(id=17, name="potato"),
    18: Ingredient(id=18, name="lettuce"),
    19: Ingredient(id=19, name="bacon"),
    20: Ingredient(id=20, name="egg"),
    21: Ingredient(id=21, name="yogurt"),
    22: Ingredient(id=22, name="lemon"),
    23: Ingredient(id=23, name="cilantro"),
    24: Ingredient(id=24, name="sesame"),
    24: Ingredient(id=25, name="strawberry"),
    24: Ingredient(id=26, name="coffee"),
    24: Ingredient(id=27, name="cream"),
    24: Ingredient(id=28, name="milk"),
    24: Ingredient(id=29, name="chocolate"),
}

# -----------------
# Restaurants (Helsinki-ish coords)
# -----------------

RESTAURANTS: Dict[int, Restaurant] = {
    1: Restaurant(id=1, name="Mama's Kitchen", lat=60.1699, lon=24.9384, type='restaurant'),
    2: Restaurant(id=2, name="Starbucks", lat=60.1705, lon=24.9410, type='starbucks'),
    3: Restaurant(id=3, name="Lola's Cafe", lat=60.1712, lon=24.9450, type='cafe'),
    4: Restaurant(id=4, name="Tokyo Noodle Bar", lat=60.1685, lon=24.9340, type='restaurant'),
    5: Restaurant(id=5, name="La Piazza", lat=60.1678, lon=24.9425, type='restaurant'),
    6: Restaurant(id=6, name="Cafe Mich", lat=60.1720, lon=24.9390, type='cafe'),
    7: Restaurant(id=7, name="Burger Hub", lat=60.1690, lon=24.9445, type='burger'),
    8: Restaurant(id=8, name="Taco Loco", lat=60.1730, lon=24.9370, type='restaurant'),
    9: Restaurant(id=9, name="Sea Breeze Sushi", lat=60.1702, lon=24.9475, type='restaurant'),
    10: Restaurant(id=10, name="Curry House Helsinki", lat=60.1688, lon=24.9488, type='restaurant'),
}

# -----------------
# Dishes
# -----------------
# Try to cover a variety of ingredient combos so that
# changing user prefs obviously reshuffles rankings.

DISHES: Dict[int, Dish] = {
    # Mama's Kitchen (1)
    1: Dish(
        id=1,
        restaurant_id=1,
        name="Garlic Chicken Rice Bowl",
        description="Grilled chicken with garlic, onions and steamed rice.",
        ingredient_ids=[1, 2, 3, 4],
    ),
    # 2: Dish(
    #     id=2,
    #     restaurant_id=1,
    #     name="Cheesy Onion Soup",
    #     description="Slow-cooked onion soup topped with melted cheese.",
    #     ingredient_ids=[1, 5, 9],
    # ),
    3: Dish(
        id=3,
        restaurant_id=1,
        name="Creamy Mushroom Chicken",
        description="Pan-seared chicken in a creamy mushroom sauce.",
        ingredient_ids=[3, 9, 10, 2],
    ),

    # Spice Route (2)
    4: Dish(
        id=4,
        restaurant_id=2,
        name="Strawberry Frappuccino",
        description="Blended ice drink with strawberry and cream",
        ingredient_ids=[2, 8, 11],
    ),
    5: Dish(
        id=5,
        restaurant_id=2,
        name="Cappuccino",
        description="Foamy coffee with milk",
        ingredient_ids=[12, 8, 1, 2],
    ),
    6: Dish(
        id=6,
        restaurant_id=2,
        name="Pain Au Chocolat",
        description="Flaky pastry with chocolate",
        ingredient_ids=[3, 22, 23],
    ),

    # Nordic Bites (3)
    7: Dish(
        id=7,
        restaurant_id=3,
        name="Salmon Potato Bake",
        description="Oven-baked salmon with creamy potatoes.",
        ingredient_ids=[16, 17, 9, 2],
    ),
    8: Dish(
        id=8,
        restaurant_id=3,
        name="Mushroom Cream Soup",
        description="Rich mushroom soup with cream and herbs.",
        ingredient_ids=[10, 9, 7],
    ),
    9: Dish(
        id=9,
        restaurant_id=3,
        name="Nordic Shrimp Salad",
        description="Shrimp, lettuce and lemon dressing.",
        ingredient_ids=[15, 18, 22],
    ),

    # Tokyo Noodle Bar (4)
    10: Dish(
        id=10,
        restaurant_id=4,
        name="Tonkotsu Ramen",
        description="Rich pork broth ramen with egg and garlic oil.",
        ingredient_ids=[13, 11, 20, 2],
    ),
    11: Dish(
        id=11,
        restaurant_id=4,
        name="Spicy Miso Tofu Ramen",
        description="Tofu ramen with chili, garlic and sesame.",
        ingredient_ids=[14, 11, 8, 2, 24],
    ),
    12: Dish(
        id=12,
        restaurant_id=4,
        name="Garlic Butter Shrimp Udon",
        description="Thick udon with garlic butter shrimp.",
        ingredient_ids=[15, 11, 2, 9],
    ),

    # La Piazza (5)
    13: Dish(
        id=13,
        restaurant_id=5,
        name="Margherita Pizza",
        description="Classic pizza with tomato, basil and mozzarella cheese.",
        ingredient_ids=[5, 6, 7],
    ),
    14: Dish(
        id=14,
        restaurant_id=5,
        name="Four Cheese Pizza",
        description="Rich mix of cheeses on a crispy crust.",
        ingredient_ids=[5, 9],
    ),
    15: Dish(
        id=15,
        restaurant_id=5,
        name="Garlic Shrimp Pasta",
        description="Pasta with garlic, shrimp and cream sauce.",
        ingredient_ids=[2, 15, 9, 11],
    ),

    # Green Garden Vegan (6)
    16: Dish(
        id=16,
        restaurant_id=6,
        name="Tofu Veggie Bowl",
        description="Tofu with mushrooms, lettuce and rice.",
        ingredient_ids=[14, 10, 18, 4],
    ),
    17: Dish(
        id=17,
        restaurant_id=6,
        name="Spicy Tofu Noodles",
        description="Vegan noodles with tofu, chili and sesame.",
        ingredient_ids=[14, 11, 8, 24],
    ),
    18: Dish(
        id=18,
        restaurant_id=6,
        name="Lemon Herb Salad",
        description="Fresh lettuce with lemon and herbs.",
        ingredient_ids=[18, 22, 7],
    ),

    # Burger Hub (7)
    19: Dish(
        id=19,
        restaurant_id=7,
        name="Classic Beef Burger",
        description="Beef patty with cheese, onion and lettuce.",
        ingredient_ids=[12, 5, 1, 18],
    ),
    20: Dish(
        id=20,
        restaurant_id=7,
        name="Bacon Mushroom Burger",
        description="Beef burger with bacon, mushrooms and cheese.",
        ingredient_ids=[12, 19, 10, 5],
    ),
    # 21: Dish(
    #     id=21,
    #     restaurant_id=7,
    #     name="Garlic Fries",
    #     description="Crispy fries tossed with garlic and herbs.",
    #     ingredient_ids=[17, 2, 7],
    # ),

    # Taco Loco (8)
    22: Dish(
        id=22,
        restaurant_id=8,
        name="Beef Tacos",
        description="Soft tacos with beef, onion, cilantro and chili salsa.",
        ingredient_ids=[12, 1, 23, 8],
    ),
    # 23: Dish(
    #     id=23,
    #     restaurant_id=8,
    #     name="Chicken Tacos",
    #     description="Chicken tacos with lettuce and tomato salsa.",
    #     ingredient_ids=[3, 18, 6, 23],
    # ),
    24: Dish(
        id=24,
        restaurant_id=8,
        name="Garlic Shrimp Tacos",
        description="Shrimp tacos with garlic and cilantro.",
        ingredient_ids=[15, 2, 23],
    ),

    # Sea Breeze Sushi (9)
    25: Dish(
        id=25,
        restaurant_id=9,
        name="Salmon Nigiri Set",
        description="Fresh salmon nigiri with rice.",
        ingredient_ids=[16, 4],
    ),
    26: Dish(
        id=26,
        restaurant_id=9,
        name="Shrimp Tempura Roll",
        description="Crispy shrimp roll with sesame.",
        ingredient_ids=[15, 24, 4],
    ),
    27: Dish(
        id=27,
        restaurant_id=9,
        name="Tofu Avocado Maki",
        description="Vegan maki with tofu and lettuce.",
        ingredient_ids=[14, 18, 4],
    ),

    # Curry House Helsinki (10)
    28: Dish(
        id=28,
        restaurant_id=10,
        name="Butter Chicken",
        description="Creamy tomato butter chicken with rice.",
        ingredient_ids=[3, 6, 9, 2, 4],
    ),
    29: Dish(
        id=29,
        restaurant_id=10,
        name="Garlic Chili Paneer (Tofu Demo)",
        description="Spicy garlic chili tofu curry.",
        ingredient_ids=[14, 2, 8, 6],
    ),
    30: Dish(
        id=30,
        restaurant_id=10,
        name="Yogurt Lemon Chicken",
        description="Chicken marinated in yogurt and lemon.",
        ingredient_ids=[3, 21, 22, 2],
    ),
}

# -----------------
# Users (demo)
# -----------------

USERS: Dict[int, UserProfile] = {
    1: UserProfile(
        id=1,
        name="Demo User",
        preferences=[
            # Demo 1: hates onion, loves garlic + chicken
            UserPreference(ingredient_id=1, weight=-0.8),  # hates onion
            UserPreference(ingredient_id=2, weight=0.7),   # likes garlic
            UserPreference(ingredient_id=3, weight=0.8),   # likes chicken
            UserPreference(ingredient_id=15, weight=0.3),  # mild shrimp fan
        ],
    ),
    2: UserProfile(
        id=2,
        name="Hater",
        preferences=[
            UserPreference(ingredient_id=2, weight=-1.0),   # loves garlic
            UserPreference(ingredient_id=15, weight=-1.0),  # loves shrimp
            UserPreference(ingredient_id=3, weight=-1.0),   # okay with chicken
            UserPreference(ingredient_id=1, weight=-1.0),  # dislikes onion
        ],
    ),
    3: UserProfile(
        id=3,
        name="Onion & Beef Lover",
        preferences=[
            UserPreference(ingredient_id=1, weight=0.8),   # loves onion
            UserPreference(ingredient_id=12, weight=0.9),  # loves beef
            UserPreference(ingredient_id=8, weight=0.4),   # likes chili
            UserPreference(ingredient_id=14, weight=-0.5), # dislikes tofu
        ],
    ),
}

# -----------------
# Quests (initial demo quest)
# -----------------

QUESTS: Dict[int, Quest] = {
    1: Quest(
        id=1,
        user_id=1,
        title="Try 2 new garlic dishes",
        steps=[
            QuestStep(
                id=1,
                description="Try Garlic Chicken Rice Bowl",
                restaurant_id=1,
                dish_id=1,
            ),
            QuestStep(
                id=2,
                description="Try Spicy Garlic Noodles",
                restaurant_id=2,
                dish_id=4,
            ),
        ],
    )
}
