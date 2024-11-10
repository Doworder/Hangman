import configparser
import random


def mask(string: str):
    return [" _ " * len(string)]


def input_validation(simbol, locale):
    if "а" <= simbol <= "я" or simbol == "ё":
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()  # parser object
        config.read("settings.ini")

        while True:
            user_answer = input("Сыграем?(д/н):")
            if user_answer == "n" or user_answer == "н":
                # is_gameover = True
                break

            with open(config["Settings"]["dictionary"]) as file:
                word = random.choice(file.readlines())

            errors_count = 0
            while errors_count < 6:
                print(*mask(word))
                letter = input("Введите букву: ")
                if not input_validation(letter, config["Settings"]["locale"]):
                    continue
                if letter in word:
                    print(mask(word))
                else:
                    errors_count += 1
                print(f"Количество ошибок: ", errors_count)

    except Exception as e:
        print("Возникла ошибка", e)

    finally:
        exit(0)
