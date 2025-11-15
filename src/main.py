from pathlib import Path
import json
import pandas as pd


# Project + data paths
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"


def load_csv(name: str) -> pd.DataFrame:
    """Load a CSV from the data directory."""
    path = DATA_DIR / name
    print(f"Loading CSV: {path}")
    return pd.read_csv(path)


def load_json(name: str):
    """Load a JSON file from the data directory."""
    path = DATA_DIR / name
    print(f"Loading JSON: {path}")
    with open(path, "r") as f:
        return json.load(f)


def describe_json(name: str, data):
    """Print a short description of JSON structure."""
    print(f"\n{name}:")
    if isinstance(data, dict):
        print("  Type: dict")
        keys = list(data.keys())
        print(f"  Keys (up to 10): {keys[:10]}")
    elif isinstance(data, list):
        print("  Type: list")
        print(f"  Length: {len(data)}")
        if len(data) > 0 and isinstance(data[0], dict):
            fields = list(data[0].keys())
            print(f"  Fields in first element: {fields}")
    else:
        print(f"  Type: {type(data)}")


def main():
    print("Hello from your new project!")
    print("VIPR test commit")
    print("VS_Code test Git commit 2a")

    # ---- Load CSVs ----
    df_games_with_ratings = load_csv("games_with_ratings.csv")
    df_pickleball_games = load_csv("pickleball_games.csv")
    df_player_ratings = load_csv("player_ratings.csv")

    # ---- Load JSONs ----
    json_games_with_ratings = load_json("games_with_ratings.json")
    json_pickleball_games = load_json("pickleball_games.json")
    json_player_ratings = load_json("player_ratings.json")

    # ---- Summaries ----
    print("\n=== CSV Data Loaded ===")
    print("games_with_ratings.csv:", df_games_with_ratings.shape)
    print("pickleball_games.csv:  ", df_pickleball_games.shape)
    print("player_ratings.csv:    ", df_player_ratings.shape)

    print("\n=== JSON Data Loaded ===")
    describe_json("games_with_ratings.json", json_games_with_ratings)
    describe_json("pickleball_games.json", json_pickleball_games)
    describe_json("player_ratings.json", json_player_ratings)


if __name__ == "__main__":
    main()
