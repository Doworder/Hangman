from configparser import ConfigParser
from random import choice

from hangman.graphics import HANGMAN_GRAPHICS as GRAPHIC_STATE  # type: ignore


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


def is_hidden_word(user_input: str, hidden_word: str) -> bool:
    if user_input == hidden_word:
        return True

    else:
        return False


def is_one_symbol(user_input: str) -> bool:
    if len(user_input) != 1:
        print("Введите одну букву")

        return False

    else:
        return True


def is_entered_letters(user_input: str, entered_letters: set) -> bool:
    if user_input in entered_letters:
        print("Вы уже вводили эту букву!")

        return True

    else:
        return False


def is_validate_input(user_input: str, entered_letters: set, hidden_word: str) -> bool:  # type: ignore
    if is_hidden_word(user_input, hidden_word):
        return True

    elif user_input.isalpha():
        if is_one_symbol(user_input):
            if not is_entered_letters(user_input, entered_letters) and is_cyrillic_symbol(user_input):
                return True

    else:
        print("Это не буква!")
        return False


def make_input(entered_letters: set, hidden_word: str) -> str:
    while True:
        user_input = input("Введите букву: ").lower()
        if is_validate_input(user_input, entered_letters, hidden_word):
            return user_input


def is_cyrillic_symbol(symbol: str, ) -> bool:
    if "а" <= symbol <= "я" or symbol == "ё":
        return True

    else:
        print("Введите букву русского алфавита")
        return False


def show_hangman_state(state: int) -> None:
    print(GRAPHIC_STATE[state])


def play_game(hidden_word: str) -> None:

    errors_count: int = 0
    entered_letters: set[str] = set()

    mask: list[str] = [MASK_SYMBOL] * len(hidden_word)

    while MASK_SYMBOL in str(mask) and errors_count < 6:
        show_hangman_state(errors_count)
        print(*mask)

        letter: str = make_input(entered_letters, hidden_word)
        entered_letters.add(letter)
        if is_hidden_word(letter, hidden_word):
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

        hidden_word: str = get_word("data/" + GAME_DICTIONARY_NAME)

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
        SETTINGS_FILE: str = "config.ini"
        MASK_SYMBOL: str = get_setting(SETTINGS_FILE, "Settings", "mask_symbol")
        GAME_DICTIONARY_NAME: str = get_setting("config.ini", "Settings", "dictionary")

        start_game()

    except Exception as e:
        print("Возникла ошибка", e)
        exit(1)

    finally:
        exit(0)
