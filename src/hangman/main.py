from configparser import ConfigParser
from random import choice

from hangman.graphics import HANGMAN_GRAPHICS as GRAPHIC_STATE


def get_config(path: str) -> ConfigParser:
    config = ConfigParser()
    config.read(path)
    return config


def get_setting(path: str, section: str, setting: str) -> str:
    config: ConfigParser = get_config(path)
    config_attribute: str = config.get(section, setting)
    return config_attribute


def get_word(dictionary_path: str) -> str:
    try:
        with open(dictionary_path) as file:
            word: str = choice(file.read().splitlines())
        return word

    except FileNotFoundError:
        print('Не найден файл со словами для игры! Обратитесь к разработчику')
        return ''


def update_mask(letter: str, hidden_word: str, mask: list[str]) -> None:
    for i, symbol in enumerate(hidden_word):
        if letter == symbol:
            mask[i] = letter


def make_input(entered_letters: set, hidden_word: str) -> str:
    while True:
        input_data = input("Введите букву: ").lower()
        if input_data == hidden_word:
            return input_data
        elif len(input_data) > 1:
            print("Введите одну букву")
        elif input_data in entered_letters:
            print("Вы уже вводили эту букву!")
        elif input_data.isalpha():
            entered_letters.add(input_data)
            return input_data
        else:
            print("Это не буква!")


def is_cyrillic_symbol(symbol: str, ) -> bool:
    if "а" <= symbol <= "я" or symbol == "ё":
        return True
    else:
        print("Введите букву русского алфавита")
        return False


def show_hangman_state(state: int) -> None:
    print(GRAPHIC_STATE[state])


def play_game(hidden_word: str) -> None:
    settings_file: str = "config.ini"
    errors_count: int = 0
    entered_letters: set[str] = set()
    mask_symbol: str = get_setting(settings_file, "Settings", "mask_symbol")

    mask: list[str] = [mask_symbol] * len(hidden_word)
    while mask_symbol in str(mask) and errors_count < 6:
        show_hangman_state(errors_count)
        print(*mask)
        letter: str = make_input(entered_letters, hidden_word)
        if letter == hidden_word:
            break
        if letter in hidden_word:
            update_mask(letter, hidden_word, mask)
        else:
            errors_count += 1

        print("Количество ошибок: ", errors_count)
    print_end_state(errors_count, entered_letters, hidden_word)


def start_game() -> None:
    while True:
        user_answer: str = input("Сыграем? (Нажмите любую клавишу для продолжения ИЛИ н - для выхода): ").lower()
        if user_answer == "n" or user_answer == "н":
            break

        game_dictionary_name: str = get_setting("config.ini", "Settings", "dictionary")
        hidden_word: str = get_word("data/" + game_dictionary_name)

        play_game(hidden_word)


def print_end_state(state: int, used_letters: set[str], hidden_word: str) -> None:
    if state == 6:
        show_hangman_state(state)
        print("Вы проиграли!")
        print("Использованные буквы: ", used_letters)
        print("Загаданное слово: ", hidden_word.upper())
    else:
        print("Победа!", f"Вы отгадали слово: {hidden_word.upper()}", sep="\n")


if __name__ == "__main__":
    try:
        start_game()

    except Exception as e:
        print("Возникла ошибка", e)
        exit(1)

    finally:
        exit(0)
