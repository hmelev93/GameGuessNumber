import os
def menu():
    try:
        max_num = 100
        while True:
            os.system('cls')
            print(f"Игра 'Угадай число' позволяет вам угадывать числа в диапазоне от 1 до {max_num}.")
            print("\nМеню:")
            print("a - Играть")
            print("b - Конечное число")
            print("q - Выход")
            choice = input("Выберите действие: ").lower()
            
            match choice:
                case "a":
                    os.system('cls')
                    while True:
                        username = input("Введите ваше имя: (s - общий режим): ")
                        username = str(username)
                        if username == "s":
                            username = "no_name_mode"
                            break  # Выход из цикла, если число в пределах допустимого
                        else:
                            print(f"Здравствуй: {username}")
                            break
                    from game import play_game
                    play_game(username,max_num)
                case "b":
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
                    print(f"Вы ввели: {max_num}")
                    continue
                case "q":
                    print("Выход из игры. До свидания!")
                    break
                case _:
                    print("Некорректный ввод. Попробуйте снова.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")