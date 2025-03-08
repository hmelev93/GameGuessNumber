import os

def menu(max_num):
    last_message = ""
    try:
        while True:
            os.system('cls')
            
            print(last_message)
            print(f"Игра 'Угадай число' позволяет вам угадывать числа в диапазоне от 1 до {max_num}.")
            print("\nМеню:")
            print("w - Играть")
            print("d - Максимальное число")
            print("q - Выход")
            print("del - удалить статистику")
            choice = input("Выберите действие: ").lower()
            
            match choice:
                case "w":
                    os.system('cls')
                    while True:
                        username = input("Введите ваше имя:\n(s - общий режим): ")
                        username = str(username)
                        if username == "s":
                            username = ""
                            break  # Выход из цикла
                        else:
                            print(f"Здравствуй: {username}")
                            break
                    from game import play_game
                    play_game(username,max_num)
                case "d":
                    while True:
                        max_num = input("Введите максимальное число: ")
                        try:
                            max_num = int(max_num)
                            if 1 <= max_num <= 1000:
                                break  # Выход из цикла, если число в пределах допустимого
                            else:
                                print("Ошибка: введите число от 1 до 1000.")
                        except ValueError:
                            print("Ошибка: введите целое число.")
                    last_message = f"Вы ввели: {max_num}"
                    continue
                case "q":
                    print("Выход из игры. До свидания!")
                    exit()
                    
                case "del":
                    pwd = input("пароль: ")
                    if pwd == "1234":
                        # if os.path.exists("game_state.json"):
                        os.remove("game_state.json")
                        last_message = "...вся статистика удалена"
                        continue
                    else:
                        last_message = "неправильный пароль"
                        continue
                case _:
                    last_message= "Некорректный ввод. Попробуйте снова."
    except KeyboardInterrupt:
        print("\nВыход из программы.")