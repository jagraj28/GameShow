import random
import operator
import time
import csv

operators = {"+":operator.add, "-":operator.sub, "*":operator.mul}

class1 = {}
class2 = {}    
class3 = {}
averages = {}

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

    # User's Class
    validClass = False
    while validClass == False:
        try:
            className = str(input("What class are you in; 1, 2 or 3?: "))
            if userName.isalpha():
                validClass = True
        except ValueError:
            print("Erm, that's not a real class! Try again!")

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

# Saving Names and Scores
def Scores():

    # Run Intro and Quiz functions
    userName, className = Introduction() 
    score = Quiz()

    # Saving Name and Score to dictionary
    if className == "1":
        class1.setdefault(userName, [])
        class1[userName].append(score)
    else:
        print("Sorry, class is not valid, scores not saved!")
    if className == "2":
        class2.setdefault(userName, [])
        class2[userName].append(score)
    else:
        print("Sorry, class is not valid, scores not saved!")
    if className == "3":
        class3.setdefault(userName, [])
        class3[userName].append(score)
    else:
        print("Sorry, class is not valid, scores not saved!")
    
    return(userName, className, score)

# Writing Info to Excel File
def File():

    # Run Intro, Quiz and Scores functions
    userName, className, score = Scores()

    # Check if user wishes to re-try quiz
    while True:
        try:
            endProgram = input("Do you wish to exit the quiz? Y or N: ")
            break
        except ValueError:
            endProgram = input("Enter a valid answer: ")
            break
    
    # Writing to file
    if endProgram == "Y" and className == "1":
        with open("Class 1 Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(class1.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!\n")
        File()
    else:
        print("Error, file not created!")
    if endProgram == "Y" and className == "2":
        with open("Class 2 Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(class2.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!\n")
        File()
    else:
        print("Error, file not created!")
    if endProgram == "Y" and className == "3":
        with open("Class 3 Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(class3.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!\n")
        File()
    else:
        print("Error, file not created!")

def Teacher():

    # Check if user is teacher or student
    try:
        is_teacher = input("Are you a teacher or student? Reply with S or T: ")
    except ValueError:
        is_teacher = input("Enter a valid answer: ")

    # Run Quiz if not teacher
    if is_teacher == "S":
        File()

    # Ask if teacher wishes to see scores
    try:
        CheckScores = input("Do you wish to check class scores? Y or N: ")
    except ValueError:
        CheckScores = input("Enter a valid answer: ")

    # Open CSV files and print names and scores dependent on class
    if is_teacher == "T" and CheckScores == "Y":
        try:
            which_class = input("Which class scores would you like to view: ")
        except ValueError:
            which_class = input("Enter a valid answer: ")
        if which_class == "1":
                with open(r"Class 1 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=',', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
        if which_class == "2":
                with open(r"Class 2 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=',', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
        if which_class == "3":
                with open(r"Class 3 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=',', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
    
    # Stop the program if teacher doesn't wish to see scores.
    elif CheckScores == "N":
        print("You have exited the program.")

Teacher()
