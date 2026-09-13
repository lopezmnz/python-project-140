import random
import prompt

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def generate_question():
    return random.randint(1, 100)


def play_round():
    number = generate_question()
    print(f"Question: {number}")

    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    answer = prompt.string('Your answer: ')

    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(
            f"'{answer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        result = play_round()

        if not result:
            break

    if result:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()