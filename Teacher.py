import csv
from File import File

def Teacher():

    # Check if user is teacher or student
    try:
        is_teacher = input("Are you a teacher or student? Reply with S or T: ")
    except ValueError:
        is_teacher = input("Enter a valid answer: ")

    # Run Quiz if not teacher
    if is_teacher == "S":
        File()

    # Open CSV files and print names and scores
    if is_teacher == "T":
        try:
            CheckScores = str(input("Do you wish to check class scores? Y or N: "))
        except ValueError:
            CheckScores = str(input("Enter a valid answer: "))
        if CheckScores == "Y":
            with open(r"Class Scores.csv") as f:
                reader = csv.reader(f, delimiter=' ', quotechar='|')
                for row in reader:
                    print(row)
        elif CheckScores == "N":
            print("You have exited the program.")