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

def reload_game(games_count,username,filename="game_state.json"):
    data = load_game(filename) or {}
    data.pop(username, None)
    games_count += 1
    with open("game_state.json", "w") as f:
        data[username] = {"game_count": games_count}
        json.dump(data, f)
