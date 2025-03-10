# Обзор проекта

## Цель проекта

Этот проект реализует игру «Угадайте число». 
  - Позволяет пользователям играть
  - Сохранять свой прогресс и возобновить игры позже.
  - Игра предоставляет удобное меню для навигации на различные варианты, включая запуск новой игры, изменение сложности и управление статистикой игры.

## Ключевые функции

* **Логика игры:** позволяет пользователям угадать число в указанном диапазоне, предоставляя обратную связь о том, слишком ли их предположение высокое или слишком низкое.
* **Сохранить/загрузить состояние игры:** позволяет пользователям сохранять свой текущий прогресс в игре (загаданное число, попытки, история игр) и возобновить его позже.
* **Регулируемая сложность:** Пользователи могут изменить максимальное число для диапазона догадок, эффективно контролируя сложность игры.
* **Меню, удобное для пользователя:** предоставляет четкое и интуитивно понятное меню для навигации по функциям игры.
* **Управление статистикой игры:** Позволяет пользователям удалять свою статистику игры.

## Архитектура

Приложение следует модульной конструкции, разделяя проблемы на различные файлы.
 -`main.py` служит точкой входа, инициализация игры и вызов функции« меню ». 
 - Файл `menu.py` обрабатывает взаимодействие с пользователем, представляя параметры и направляя пользователя к соответствующим игровым функциям.
 - Основная игровая логика находится в `game.py`, управляя циклом игры, пользовательским вводом и условиями победы/проигрыша.
 - Наконец, `storage.py` обрабатывает устойчивость состояний игры, позволяя пользователям сохранять и загружать свой прогресс.
 - Модули сообщаются друг с другом, чтобы обеспечить успешный игровой опыт.

## Технический стек

* **Язык:** Python
* **Модули/библиотеки:**
    * `random`: для генерации секретного числа.
    * `os`: для очистки экрана консоли.
    * `json`: для сохранения и загрузки игровых данных в формате JSON.
* **Дизайн проекта:** Проект использует модульный дизайн, способствуя повторной использованию кода и обслуживаемости.

## Быстрый старт

1. **Клонируйте репозиторий:** `git clone https://github.com/hmelev93/GameGuessNumber.git` (замените на фактический URL -адрес).
2. **Перейдите к каталогу проекта:** `CD [Project_Directory]`
3. **Запустите основной сценарий:** `python main.py`
4. Появится меню игры, что позволит вам запустить новую игру, изменить настройки или уйти.

## Структура проекта

Проект организован в следующие файлы:

* `main.py`: точка входа приложения.
* `menu.py`: обрабатывает основное меню и взаимодействие с пользователем.
* `game.py`: содержит основную игровой логику.
* `storage.py`: управляет сохранением и загрузкой игровых данных.
