import random
import prompt

number = random.randint(1, 100)

Answer = ""

if number %2 ==0:
    Answer = "yes"
else:   
    Answer = "no"
    
print(f"Question: {number}")

 
Answe1 = prompt.string("Your answer: ")

if Answe1 == Answer:
    print("Correct!")  
else:
    print(f"'{Answe1}' is wrong answer ;(. Correct answer was '{Answer}'.")
    
    