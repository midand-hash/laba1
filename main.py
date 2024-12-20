import random


def guess_the_number():
    number_to_guess = random.randint(1, 50)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        user_guess = input("Введите ваше число: ")

        # Проверяем, является ли ввод числом
        try:
            user_guess = int(user_guess)
            attempts += 1
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        if user_guess < number_to_guess:
            print("Слишком низко, попробуйте еще раз.")
        elif user_guess > number_to_guess:
            print("Слишком высоко, попробуйте еще раз.")
        else:
            print(f"Вы угадали! Загаданное число: {number_to_guess}. Попытки: {attempts}")
            break


guess_the_number()