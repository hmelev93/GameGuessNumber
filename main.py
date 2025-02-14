import random
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


def play_game(username):
    

    data = load_game()
    user_data = data.get(username, {})
    secret_number = user_data.get("secret_number", random.randint(1, 100))
    attempts = user_data.get("attempts", 0)
    games_count = user_data.get("games", 1)
    history = user_data.get("history", [])
    max_attempts = 10

    if attempts < 1:
        print(f"Добро пожаловать в игру 'Угадай число', {username}!")
        print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    while attempts < max_attempts:
        try:
            guess = input("Введите число от 1 до 100 \n q - выход\n5 ")
            if guess.lower() == "q":
                save_game({"secret_number": secret_number, "attempts": attempts, "history": history, "games": games_count}, username)
                print("Игра сохранена. До встречи!")
                return

            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Пожалуйста, введите число от 1 до 100.")
                continue

            attempts += 1
            history.append(guess)
            if guess < secret_number:
                print("Слишком маленькое!")
            elif guess > secret_number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю, {username}! Вы угадали число {secret_number} за {attempts} попыток!")
                data.pop(username, None)
                with open("game_state.json", "w") as f:
                    games_count += 1
                    data[username] = {"game_count": games_count}
                    json.dump(data, f)
                return

            print(f"Осталось попыток: {max_attempts - attempts}")

        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"Вы исчерпали {max_attempts} попыток. Загаданное число было {secret_number}.")
    data.pop(username, None)
    with open("game_state.json", "w") as f:
        games_count += 1
        data[username] = {"game_count": games_count}
        json.dump(data, f)


def main():
    username = input("Введите ваше имя: ")
    data = load_game()
    if username in data:
        if "attempts" in data[username]:
            print(f"Продолжаем игру, {username}! Попыток использовано: {data[username]['attempts']}")
            play_game(username)
        else:
            play_game(username)
        return

    play_game(username)


if __name__ == "__main__":
    main()
