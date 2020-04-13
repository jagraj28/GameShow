import random
import operator
import time
import csv

Operators = {"+":operator.add, "-":operator.sub, "*":operator.mul}

# Introduction
def Introduction():
    print("Welcome to the quiz!")

    # User's Name
    ValidName = False
    while ValidName == False:
        try:
            userName = str(input("What's your name?: "))
            if userName.isalpha():
                ValidName = True
        except ValueError:
            print("Ah come on, that's not a name! Try again!")
            continue

    # User's Class
    ValidClass = False
    while ValidClass == False:
        try:
            className = str(input("What class are you in?: "))
            if userName.isalpha():
                ValidClass = True
        except ValueError:
            print("Erm, that's not a real class! Try again!")
            continue

    print("Great! The quiz will now begin, good luck!")
    return(userName, className)

Introduction()