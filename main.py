import configparser
import random
import graphics


def get_config(path):
    # if not os.path.exists(path):
    #     create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    config = get_config(path)
    value = config.get(section, setting)
    # msg = "{section} {setting} is {value}".format(
    #     section=section, setting=setting, value=value
    # )
    #
    # print(msg)
    return value


def get_word(dictionary):
    with open(dictionary) as file:
        word = random.choice(file.read().splitlines())
    return word


def update_mask(string: str):
    for i, item in enumerate(hidden_word):
        if string == item:
            hidden_mask[i] = string


def input_validation(string):
    if len(string) == 1 or len(string) == len(hidden_word):
        if "а" <= string <= "я" or string == "ё":
            return True
    else:
        return False


def hangman_rendering(state):
    print(graphics.hangman_graphics[state])


if __name__ == "__main__":
    try:
        while True:
            user_answer = input("Сыграем?(д/н):").lower()
            if user_answer == "n" or user_answer == "н":
                break

            game_dictionary = get_setting("settings.ini", "Settings", "dictionary")
            hidden_word = get_word(game_dictionary)

            errors_count = 0
            entered_letters = []
            hidden_mask = [" _ "] * len(hidden_word)
            while errors_count < 6:
                hangman_rendering(errors_count)
                print(*hidden_mask)
                letter = input("Введите букву: ").lower()
                if not input_validation(letter):
                    continue
                if letter == hidden_word:
                    break
                if letter in hidden_word:
                    update_mask(letter)
                else:
                    if letter not in entered_letters:
                        errors_count += 1
                        entered_letters.append(letter)
                print("Количество ошибок: ", errors_count)
                if " _ " not in hidden_mask:
                    print(*hidden_mask)
                    break

            if errors_count == 6:
                hangman_rendering(errors_count)
                print("Вы проиграли!")
                print("Использованные буквы: ", entered_letters)
                print("Загаданное слово: ", hidden_word.upper())
            else:
                print("Победа!", "Вы отгадали слово", sep="\n")

    except Exception as e:
        print("Возникла ошибка", e)
        exit(1)

    finally:
        exit(0)
