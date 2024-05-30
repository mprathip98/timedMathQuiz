import random
import time
import math
welcome = input("Would you like to play the timed math game? ")
if welcome != "yes":
    quit()



problemsNum = 0
score = 0
time0 = time.time()
while problemsNum != 10:


    operators = ["+", "-", "*", "/"]
    operatorValue = operators[random.randrange(0, 3)]
    minValue = random.randrange(0, 12)
    maxValue = random.randrange(0, 12)

    question = str(minValue) + " " + operatorValue + " " + str(maxValue)
    answer = eval(question)

    userAnswer = input("Question: " + question + " ")

    if str(userAnswer) == str(answer):
        print("Correct! \n")
        score += 1
        pass
    else:
        print("--- INCORRECT! ---\n")

    problemsNum += 1
    time1 = time.time()


else:
    print(f"It took you {math.ceil(time1 - time0)} seconds")
    print(f"Your Score: {score} out of 10")