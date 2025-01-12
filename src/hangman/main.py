from configparser import ConfigParser
from random import choice

from graphics import hangman_graphics as graph


def get_config(path: str) -> ConfigParser:
    config = ConfigParser()
    config.read(path)
    return config


def get_setting(path: str, section: str, setting: str) -> str:
    config = get_config(path)
    value = config.get(section, setting)
    return value


def get_word(dictionary_path: str) -> str:
    try:
        with open(dictionary_path) as file:
            word = choice(file.read().splitlines())
        return word

    except FileNotFoundError:
        print(f'Не найден файл со словами для игры! Обратитесь к разработчику')


def update_mask(string: str, hidden_word: str, hidden_mask: list[str]) -> None:
    for i, item in enumerate(hidden_word):
        if string == item:
            hidden_mask[i] = string



def input_validation(string: str, hidden_word: str) -> bool:  # TODO rename, peredelat voobshe
    if len(string) == 1 or len(string) == len(hidden_word):
        if "а" <= string <= "я" or string == "ё":
            return True
        else:
            print("Введите букву русского алфавита")
            return False
    else:
        print("Введите одну букву")
        return False


def hangman_rendering(state: int) -> None:
    print(graph[state])


def game(hidden_word: str) -> None:
    errors_count: int = 0
    entered_letters: set[str] = set()
    mask_symbol: str = get_setting("config.ini", "Settings", "mask_symbol")
    hidden_mask: list[str] = [mask_symbol] * len(hidden_word)
    while errors_count < 6 and (mask_symbol in str(hidden_mask)):
        hangman_rendering(errors_count)
        print(*hidden_mask)
        letter = input("Введите букву: ").lower()
        if not input_validation(letter, hidden_word):
            continue
        if letter == hidden_word:
            break
        if letter in hidden_word:
            update_mask(letter, hidden_word, hidden_mask)
        else:
            if letter not in entered_letters:
                errors_count += 1
                entered_letters.add(letter)
        print("Количество ошибок: ", errors_count)
        # if " _ " not in hidden_mask:
        #     print(*hidden_mask)
        #     break

    if errors_count == 6:
        hangman_rendering(errors_count)
        print("Вы проиграли!")
        print("Использованные буквы: ", entered_letters)
        print("Загаданное слово: ", hidden_word.upper())
    else:
        print("Победа!", "Вы отгадали слово", sep="\n")


def start_game() -> None:
    while True:
        user_answer = input("Сыграем? (Нажмите любую клавишу для продолжения ИЛИ н - для выхода): ").lower()
        if user_answer == "n" or user_answer == "н":
            break

        game_dictionary = get_setting("config.ini", "Settings", "dictionary")
        hidden_word = get_word("data/" + game_dictionary)

        game(hidden_word)


if __name__ == "__main__":
    start_game()
    # try:
    #     start_game()
    #
    # except Exception as e:
    #     print("Возникла ошибка", e)
    #     exit(1)
    #
    # finally:
    #     exit(0)
