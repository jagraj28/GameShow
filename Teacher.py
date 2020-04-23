import csv
from File import File

# Student or Teacher function
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
            which_class = int(input("Which class scores would you like to view: "))
        except ValueError:
            which_class = input("Enter a valid answer: ")
        if which_class == "1":
                with open(r"Class 1 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=' ', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
        if which_class == "2":
                with open(r"Class 2 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=' ', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
        if which_class == "3":
                with open(r"Class 3 Scores.csv") as f:
                    reader = csv.reader(f, delimiter=' ', quotechar='|')
                    print("In Alphabetical Order:")
                    for row in reader:
                        print(row)
    
    # Stop the program if teacher doesn't wish to see scores.
    elif CheckScores == "N":
        print("You have exited the program.")