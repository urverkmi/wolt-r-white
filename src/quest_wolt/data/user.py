from pathlib import Path
import json
from typing import Dict

from pandas.io.formats.format import return_docstring

from utils import from_ingredient_id_to_human

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "files"
USER_PREF_PATH = DATA_DIR / "user_prefs.json"

def get_user_pref_dict(user_id) -> Dict[str, float]:
    """
    Load the big JSON and return the preference dict for a single user.

    JSON structure:
    {
      "0": {"1124": -0.01, "2805": ...},
      "1": {"2518": -0.0096, ...},
      ...
    }
    """
    with USER_PREF_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    # user_id may be int or str; JSON keys are strings
    return data.get(str(user_id), {})


def get_user_pref_dict_human_readable(user_prefs: Dict[str, float]) -> Dict[str, float]:
    """
    Convert a {ingredient_id_str: weight} dict into
    {human_ingredient_name: weight}.
    """
    human_prefs: Dict[str, float] = {}

    for ingr_id, weight in user_prefs.items():
        try:
            human_name = from_ingredient_id_to_human(str(ingr_id))
        except KeyError:
            human_name = f"UNKNOWN_{ingr_id}"

        human_prefs[human_name] = weight

    return human_prefs

if __name__ == "__main__":
    print(get_user_pref_dict("1"))
