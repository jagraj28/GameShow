from Introduction import Introduction
from Quiz import Quiz

class1 = {}
class2 = {}    
class3 = {}

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