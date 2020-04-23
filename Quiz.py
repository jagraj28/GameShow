import random
import operator

operators = {"+":operator.add, "-":operator.sub, "*":operator.mul}

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
                userAns = int(input("Enter your answer: "))
                break
            except ValueError:
                userAns = int(input("Enter a valid answer: "))
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