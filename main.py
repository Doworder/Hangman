is_gameover = False  # TODO кажется это лишнее


if __name__ == "__main__":
    while not is_gameover:
        user_answer = input("Сыграем?(д/н):")
        if user_answer == "n" or user_answer == "н":
            is_gameover = True
            break

        errors_count = 0
        while errors_count < 6:
            print(f"Количество ошибок: ", errors_count)
            errors_count += 1

    exit(0)
