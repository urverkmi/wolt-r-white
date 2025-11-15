from pydantic import BaseModel
from typing import List, Dict, Optional
from typing import List

class Ingredient(BaseModel):
    id: int
    name: str

class Dish(BaseModel):
    id: int
    restaurant_id: int
    name: str
    description: str
    ingredient_ids: List[int] = []

class Restaurant(BaseModel):
    id: int
    name: str
    lat: float
    lon: float

class UserPreference(BaseModel):
    ingredient_id: int
    weight: float  # -1.0 (hate) to 1.0 (love)

class UserProfile(BaseModel):
    id: int
    name: str
    preferences: List[UserPreference] = []

class DishFeedback(BaseModel):
    dish_id: int
    rating: int  # 1-5, for demo

class QuestStep(BaseModel):
    id: int
    description: str
    restaurant_id: int
    dish_id: Optional[int] = None
    status: str = "pending"  # pending / completed

class Quest(BaseModel):
    id: int
    user_id: int
    title: str
    steps: List[QuestStep]
    status: str = "active"  # active / completed

class UpdatePreferencesRequest(BaseModel):
    preferences: List[UserPreference]

class UpdateQuestRequest(BaseModel):
    step_id: Optional[int] = None
    status: Optional[str] = None  # e.g. "completed"