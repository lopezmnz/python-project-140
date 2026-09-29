import random
import prompt   

number = random.randint(1, 100)

print(f"Answer:{number}")

if number % 2 == 0:
    correct_answer = "yes"
else:
    correct_answer = "no"

print(f"correct answer: {correct_answer}")
