import random
import os
from menu import menu
from storage import save_game, load_game, reload_game

def play_game(username,max_num):
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до {max_num}. Попробуйте угадать его!")
    
    data = load_game()
    user_data = data.get(username, {})
    secret_number = user_data.get("secret_number", random.randint(1, 100))
    attempts = user_data.get("attempts", 0)
    max_num = user_data.get("max_num", 100)
    games_count = user_data.get("games_count", 1)
    history = user_data.get("history", [])
    
    max_attempts = 10
    
    if username in data:
        if "attempts" in data[username]:
            continue_game = input(f"Попыток осталось {max_attempts - data[username]['attempts']} \nПродолжить игру?\n w - продолжить: \n q - выход: ")
            if continue_game == "w":
                pass
            else:
                reload_game(games_count,username)
                menu(max_num)

    while attempts < max_attempts:
        try:
            guess = input("Введите число ('q' - выход): ")
            if guess.lower() == "q":
                save_game({"secret_number": secret_number, "attempts": attempts, "history": history, "games_count": games_count, "max_num": max_num}, username)
                print("Игра сохранена. До встречи!")
                exit()
            guess = int(guess)
            if guess < 1 or guess > 100:
                print(f"Пожалуйста, введите число от 1 до {max_num}.")
                continue
            
            attempts += 1
            history.append(guess)
            
            if guess < secret_number:
                print("Слишком маленькое!")
            elif guess > secret_number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю, {username}! Вы угадали число {secret_number} за {attempts} попыток!")
                reload_game(games_count,username)
                restart = input(f"Сыграть еще раз? (f - продолжить | q - выход): ")
                if restart.lower() == "f":
                    menu(max_num)
                if restart.lower() == "q":
                    os.system('cls')
                    exit()
                else:
                    print("До встречи!")
                    return
  
                data.pop(username, None)  # Удаляем данные после успешной игры
                save_game(data, username)
                return
            
            print(f"Осталось попыток: {max_attempts - attempts}")
            
        except ValueError:
            print("Пожалуйста, введите целое число.")
    
    print(f"Вы исчерпали {max_attempts} попыток. Загаданное число было {secret_number}.")
    reload_game(games_count,username)
    restart = input(f"Сыграть еще раз? (f - продолжить):  ")
    if restart.lower() == "f":
        menu()
    else:
        print("До встречи!")
        return
    data.pop(username, None)
    save_game(data, username)