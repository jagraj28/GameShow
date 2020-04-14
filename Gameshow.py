import random
import operator
import time
import csv

operators = {"+":operator.add, "-":operator.sub, "*":operator.mul}

# Introduction
def Introduction():
    print("Welcome to the quiz!")

    # User's Name
    validName = False
    while validName == False:
        try:
            userName = str(input("What's your name?: "))
            if userName.isalpha():
                validName = True
        except ValueError:
            print("Ah come on, that's not a name! Try again!")
            continue

    # User's Class
    validClass = False
    while validClass == False:
        try:
            className = str(input("What class are you in?: "))
            if userName.isalpha():
                validClass = True
        except ValueError:
            print("Erm, that's not a real class! Try again!")
            continue

    # Message to start the quiz
    print("Great! The quiz will now begin, good luck!")
    return(userName, className)

# Quiz
def Quiz():
    questionNumber = 0
    score = 0

    # Question loop and random numbers generated
    while questionNumber < 10:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        operator = random.choice(list(operators.keys()))
        questionNumber += 1
        
        # Formation of question
        print(questionNumber, ")", "What is", num1, operator, num2, "?")
        ans = operators.get(operator)(num1, num2)

        # Ensure user input is valid
        while True:
            try:
                userAns = float(input("Enter your answer: "))
                break
            except ValueError:
                userAns = float(input("Enter a valid answer: "))
                break
        
        # Check user answer is correct
        if userAns == ans:
            score = score + 1
            print("Correct!")
        else:
            print("Incorrect!")
    
    # Inform user of their score
    print("Thanks for completing the quiz!", "Your score is", score, "!")
    return(score)

Introduction()
Quiz()