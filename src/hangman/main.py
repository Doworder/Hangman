from configparser import ConfigParser
from random import choice

from graphics import hangman_graphics as graph


def get_config(path: str) -> ConfigParser:
    config = ConfigParser()
    config.read(path)
    return config


def get_setting(path: str, section: str, setting: str) -> str:
    config: ConfigParser = get_config(path)
    value: str = config.get(section, setting)
    return value


def get_word(dictionary_path: str) -> str:
    try:
        with open(dictionary_path) as file:
            word: str = choice(file.read().splitlines())
        return word

    except FileNotFoundError:
        print(f'Не найден файл со словами для игры! Обратитесь к разработчику')


def update_mask(string: str, hidden_word: str, hidden_mask: list[str]) -> None:
    for i, item in enumerate(hidden_word):
        if string == item:
            hidden_mask[i] = string


def make_input(entered_letters: set, hidden_word: str, current_locale: str) -> str:
    while True:
        input_data = input("Введите букву: ").lower()
        if input_data == hidden_word:
            return input_data
        elif len(input_data) > 1:
            print("Введите одну букву")
        elif input_data in entered_letters:
            print("Вы уже вводили эту букву!")
        elif input_data.isalpha() and is_current_alphabet(current_locale, input_data):
            entered_letters.add(input_data)
            return input_data
        else:
            print("Это не буква!")


def is_current_alphabet(current_locale: str, symbol: str) -> bool:
    match current_locale:
        case "ru":
            return is_cyrillic_symbol(symbol)
        case _:
            return False


def is_cyrillic_symbol(string: str,) -> bool:
    if "а" <= string <= "я" or string == "ё":
        return True
    else:
        print("Введите букву русского алфавита")
        return False


def hangman_rendering(state: int) -> None:
    print(graph[state])


def game(hidden_word: str) -> None:
    settings_file: str = "config.ini"
    errors_count: int = 0
    entered_letters: set[str] = set()
    mask_symbol: str = get_setting(settings_file, "Settings", "mask_symbol")
    current_locale: str = get_setting(settings_file, "Settings", "locale")
    hidden_mask: list[str] = [mask_symbol] * len(hidden_word)
    while mask_symbol in str(hidden_mask) and errors_count < 6:
        hangman_rendering(errors_count)
        print(*hidden_mask)
        letter: str = make_input(entered_letters, hidden_word, current_locale)
        if letter == hidden_word:
            break
        if letter in hidden_word:
            update_mask(letter, hidden_word, hidden_mask)
        else:
            errors_count += 1

        print("Количество ошибок: ", errors_count)
    end_game(errors_count, entered_letters, hidden_word)


def start_game() -> None:
    while True:
        user_answer: str = input("Сыграем? (Нажмите любую клавишу для продолжения ИЛИ н - для выхода): ").lower()
        if user_answer == "n" or user_answer == "н":
            break

        game_dictionary: str = get_setting("config.ini", "Settings", "dictionary")
        hidden_word: str = get_word("data/" + game_dictionary)

        game(hidden_word)


def end_game(state: int, used_letters: set[str], hidden_word: str) -> None:
    if state == 6:
        hangman_rendering(state)
        print("Вы проиграли!")
        print("Использованные буквы: ", used_letters)
        print("Загаданное слово: ", hidden_word.upper())
    else:
        print("Победа!", f"Вы отгадали слово: {hidden_word.upper()}", sep="\n")


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
