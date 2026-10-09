import random

import prompt

from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def is_even(number):
    return number % 2 == 0


def play():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(ROUNDS_COUNT):
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"

        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")