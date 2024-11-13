import configparser
import random
import graphics


def update_mask(string: str):
    for i, item in enumerate(word):
        if string == item:
            hidden_mask[i] = string


def input_validation(string, locale):
    if len(string) == 1 or len(string) == len(word):
        if "а" <= string <= "я" or string == "ё":
            return True
    else:
        return False


def hangman_rendering(namber):
    print(graphics.hangman_graphics[namber])


if __name__ == "__main__":
    try:
        config = configparser.ConfigParser()  # parser object
        config.read("settings.ini")

        while True:
            user_answer = input("Сыграем?(д/н):").lower()
            if user_answer == "n" or user_answer == "н":
                break

            with open(config["Settings"]["dictionary"]) as file:
                word = random.choice(file.read().splitlines())

            errors_count = 0
            entered_letters = []
            hidden_mask = [" _ "] * len(word)
            while errors_count < 6:
                hangman_rendering(errors_count)
                print(*hidden_mask)
                letter = input("Введите букву: ").lower()
                if not input_validation(letter, config["Settings"]["locale"]):
                    continue
                if letter == word:
                    break
                if letter in word:
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
                print("Загаданное слово: ", word.upper())
            else:
                print("Победа!", "Вы отгадали слово", sep="\n")

    except Exception as e:
        print("Возникла ошибка", e)

    finally:
        exit(0)
