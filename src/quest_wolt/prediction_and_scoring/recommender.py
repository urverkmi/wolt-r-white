import joblib
import json
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer


class Recommender:
    def __init__(self, model_dir: Path):
        print("[Recommender] Loading models...")

        # 1. Load the TF-IDF vectorizer
        vectorizer_path = model_dir / "ingredient_tfidf.joblib"
        self.vectorizer: TfidfVectorizer = joblib.load(vectorizer_path)

        # 2. Load the trained user preference weights (OPTIONAL)
        prefs_path = model_dir / "user_prefs.json"
        self.user_prefs: dict[str, dict[str, float]] = {}

        if prefs_path.exists():
            try:
                with open(prefs_path, 'r', encoding="utf-8") as f:
                    self.user_prefs = json.load(f)
                print(
                    f"[Recommender] Loaded {len(self.user_prefs)} user profiles "
                    f"from {prefs_path}"
                )
            except json.JSONDecodeError:
                print("[Recommender] Warning: could not parse user_prefs.json, "
                      "starting with empty profile store.")
        else:
            print("[Recommender] No user_prefs.json found, using only runtime "
                  "preferences (demo mode).")

        # 3. Get the full feature list from the vectorizer
        self.feature_names = self.vectorizer.get_feature_names_out()
        self.ingredient_to_feature_idx = {
            name: idx for idx, name in enumerate(self.feature_names)
        }

        self.n_features = len(self.feature_names)
        print(
            f"[Recommender] Loaded vectorizer ({self.n_features} features) "
            f"and {len(self.user_prefs)} stored user profiles."
        )

    def _get_user_pref_vector(
        self,
        user_id,
        new_user_prefs,
    ) -> np.ndarray:
        """
        Builds a dense preference vector for a user.
        """
        pref_vector = np.zeros(self.n_features)

        if user_id and user_id in self.user_prefs:
            # Scenario A: Existing user from stored JSON
            prefs = self.user_prefs[user_id]
        elif new_user_prefs:
            # Scenario B: Runtime / demo preferences
            prefs = new_user_prefs
        else:
            # No prefs -> zero vector
            return pref_vector

        for ingr_id, weight in prefs.items():
            if ingr_id in self.ingredient_to_feature_idx:
                idx = self.ingredient_to_feature_idx[ingr_id]
                pref_vector[idx] = weight

        return pref_vector

    def recommend(
        self,
        dishes: list[dict],
        user_id,
        new_user_prefs,
    ):
        """
        Ranks a list of dishes for a user.
        """
        if not dishes:
            return []

        # 1. Get the user's preference vector (shape: [n_features])
        user_vector = self._get_user_pref_vector(user_id, new_user_prefs)

        # 2. Convert dish ingredient lists into TF-IDF "documents"
        dish_documents = [
            " ".join(str(i) for i in dish["ingredient_ids"]) for dish in dishes
        ]

        # 3. Transform dishes
        X_dishes = self.vectorizer.transform(dish_documents)

        # 4. Scores = dot product
        scores = X_dishes.dot(user_vector)

        ranked_dishes = []
        for i, dish in enumerate(dishes):
            ranked_dishes.append({
                **dish,
                "recommendation_score": float(scores[i]),
            })

        ranked_dishes.sort(key=lambda d: d["recommendation_score"], reverse=True)
        return ranked_dishes
    
    
# if __name__ == "__main__":
#     model_dir = Path("/home/two_play/git/wolt-r-white/src/quest_wolt/models/ai_models")
#     rec = Recommender(model_dir)
#
#     # some toy dishes using plain dicts
#     dishes = [
#         {"dish_id": "d1", "name": "Garlic Bomb", "ingredient_ids": ["5006"]},
#         {"dish_id": "d2", "name": "Onion Heaven", "ingredient_ids": ["840"]},
#     ]
#
#     # new user profile using string keys
#     new_user_prefs = {
#         "840": 1.0,   # loves onion
#         "5006": -1.0  # hates garlic
#     }
#
#     ranked = rec.recommend(dishes, new_user_prefs=new_user_prefs)
#     from pprint import pprint
#     pprint(ranked)


