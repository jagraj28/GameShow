import csv
from Scores import Scores, class1, class2, class3

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
        print("Good luck!")
        File()
    else:
        print("Error, file not created!")
    if endProgram == "Y" and className == "2":
        with open("Class 2 Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(class2.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!")
        File()
    else:
        print("Error, file not created!")
    if endProgram == "Y" and className == "3":
        with open("Class 3 Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(class3.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!")
        File()
    else:
        print("Error, file not created!")