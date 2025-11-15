from pathlib import Path
import pandas as pd
import json
from typing import Dict
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "files"

# Load the ingredient map from the pickle created in 2019
INGR_MAP: pd.DataFrame = pd.read_pickle(DATA_DIR / "ingr_map.pkl")
USER_PREF_PATH = DATA_DIR / "user_prefs.json"  #

def from_ingredient_id_to_human(ingredient_id: str) -> str:
    """
    Map an ingredient_id (e.g. '2131') to its human-readable name
    using the DataFrame loaded from ingr_map.pkl.
    """
    iid = int(ingredient_id)
    df = INGR_MAP

    # 1) Figure out which column holds the ingredient id
    if "ingredient_id" in df.columns:
        mask = df["ingredient_id"] == iid
    elif "id" in df.columns:
        mask = df["id"] == iid
    else:
        # Fallback: assume the last numeric column is the ID
        num_cols = df.select_dtypes(include="number").columns
        if len(num_cols) == 0:
            raise ValueError("No numeric columns found to use as ingredient_id.")
        id_col = num_cols[-1]
        mask = df[id_col] == iid

    row = df.loc[mask]

    if row.empty:
        raise KeyError(f"Ingredient id {ingredient_id} not found in INGR_MAP.")

    # 2) Pick the human-readable text: first object (string) column
    obj_cols = row.select_dtypes(include="object").columns
    if len(obj_cols) == 0:
        # Fallback: just return a dict-like string of the full row
        return str(row.iloc[0].to_dict())

    return str(row.iloc[0][obj_cols[0]])




if __name__ == "__main__":
    print(from_ingredient_id_to_human("600"))
#     # print(from_ingredient_id_to_human("3355"))
#     #
#     # raw_prefs = get_user_pref_dict("0")
#     # print("Raw prefs:", raw_prefs)
#     #
#     # human_prefs = get_user_pref_dict_human_readable(raw_prefs)
#     # print("\nHuman-readable prefs:")
#     # for name, w in human_prefs.items():
#     #     print(f"{name:40s} {w:.4f}")
