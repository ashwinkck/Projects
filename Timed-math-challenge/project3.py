import random

OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MAX_OPERAND,MAX_OPERAND)
    oprerator = random.choice(OPERATORS)

    


    expr = str(left) + " " + oprerator + " " + str(right)
    print(expr)
    if oprerator == OPERATORS[0]:
        answer = left + right
        print(f"The answer is {answer}")
    else:
        print("Not addition")
    return expr

generate_problem()