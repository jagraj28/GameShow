
def Introduction():
    print("Welcome to the quiz!")

    # User's Name
    while True:
        try:
            userName = input("What's your name? ")
            if userName.isalpha():
                break
            else:
                print("Ah come on, that's not a name! Try again!")
        except ValueError:
            print("Ah come on, that's not a name! Try again!")

    # User's Class
    while True:
        try:
            className = str(input("What class are you in? "))
            if className.isnumeric():
                break
            else:
                print("Erm, that's not a real class! Try again!")
        except ValueError:
            print("Erm, that's not a real class! Try again!")

    # Message to start the quiz
    print("Great! The quiz will now begin, good luck!")
    return(userName, className)