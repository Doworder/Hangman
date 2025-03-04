# Игра "Виселица"

Интерфейс - консольный. Описание правил игры на [Википедии](https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%B5%D0%BB%D0%B8%D1%86%D0%B0_(%D0%B8%D0%B3%D1%80%D0%B0)).


## Первый проект [роадмапа](https://zhukovsd.github.io/python-backend-learning-course/) Сергея Жукова:

### Функционал приложения и меню консольного интерфейса
1. При старте, приложение предлагает начать новую игру или выйти из приложения.
2. При начале новой игры, случайным образом загадывается слово, и игрок начинает процесс по его отгадыванию.
3. Игра продолжится до тех пор, пока слово не будет отгадано или количество ошибок будет меньше 6.
4. Повторно введенная буква не считается ошибкой, игра предлагает ввести букву снова.
5. После каждой введенной буквы в консоль выводится зашифрованное слово (с уже отгаданными буквами), счётчик ошибок и текущее состояние виселицы (нарисованное ASCII символами)
6. По завершении игра выводит результат и возвращается к состоянию #1 - предложение начать новую игру или выйти из приложения.

### [ТЗ проекта](https://zhukovsd.github.io/python-backend-learning-course/projects/hangman/)

## Установка

#### Клонируем репозиторий:
```shell
git clone https://github.com/Doworder/Hangman.git
```

#### Переходим в папку Hangman:
```shell
cd Hangman
```

#### Создаём виртуальное окружение:
```shell
python -m venv venv
```

#### Активируем виртуальное окружение:

Windows
```shell
venv\Scripts\activate.bat
```

Linux и MacOS
```shell
source venv/bin/activate
```

#### Запускаем установку:
```shell
pip install .
```


## Использование

#### Запускаем скрипт:
```shell
python -m src.hangman.main
```

В дальнейшем - следуем указаниям на экране.
