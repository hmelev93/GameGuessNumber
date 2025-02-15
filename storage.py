import json
import os


def save_game(state, username, filename="game_state.json"):
    data = load_game(filename) or {}
    data[username] = state
    with open(filename, "w") as f:
        json.dump(data, f)

def load_game(filename="game_state.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}
