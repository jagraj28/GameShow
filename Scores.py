from Introduction import Introduction
from Quiz import Quiz

classScores = {}

def Scores():
    userName, className = Introduction() 
    score = Quiz()

    # Saving Name and Score to dictionary
    if userName in classScores:
        classScores[userName].append(score)
    else:
        classScores[userName] = ["Class: " + str(className), "Score: " + str(score)]
    
    return(userName, className, score, classScores)