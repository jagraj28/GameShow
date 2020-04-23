import csv
from Scores import Scores

def File():
    userName, className, score, classScores = Scores()

    # Check if user wishes to re-try quiz
    while True:
        try:
            endProgram = input("Do you wish to exit the quiz? Y or N: ")
            break
        except ValueError:
            endProgram = input("Enter a valid answer: ")
            break
    
    # Writing to file
    if endProgram == "Y":
        with open("Class Scores.csv", "a+") as f:
            FileWriter = csv.writer(f)
            FileWriter.writerows(classScores.items())
        print("You can now exit the quiz, have a great day!")
    elif endProgram == "N":
        print("Good luck!")
        File()
    else:
        print("Error, file not created!")