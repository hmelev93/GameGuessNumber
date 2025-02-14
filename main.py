import random
import json
import os


def save_game(state, filename="game_state.json"):
    with open(filename, "w") as f:
        json.dump(state, f)


def load_game(filename="game_state.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None


def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуйте угадать его!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    history = []

    while attempts < max_attempts:
        try:
            guess = input("Введите число (или 'выход' для завершения игры): ")
            if guess.lower() == "выход":
                save_game({"secret_number": secret_number, "attempts": attempts, "history": history})
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
                print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
                return

            print(f"Осталось попыток: {max_attempts - attempts}")

        except ValueError:
            print("Пожалуйста, введите целое число.")

    print(f"Вы исчерпали {max_attempts} попыток. Загаданное число было {secret_number}.")


def main():
    if os.path.exists("game_state.json"):
        choice = input("Обнаружено сохранение. Хотите продолжить игру? (да/нет): ").lower()
        if choice == "да":
            state = load_game()
            if state:
                print(
                    f"Продолжаем! Загаданное число {state['secret_number']} (но вы его не видите). Попыток использовано: {state['attempts']}")
                play_game()
                os.remove("game_state.json")
                return

    play_game()


if __name__ == "__main__":
    main()
