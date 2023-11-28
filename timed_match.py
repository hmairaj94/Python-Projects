import random
import time

OPERATORS = ['+','-','*']
MIN_OPERAND = 2
MAX_OPERAND = 10
TOTAL_PROBLEMS = 5

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    expr = str(left) + " " + operator + " " + str(right) 
    answer = eval(expr) #eval basically evaluates a expression in python
    return expr , answer    

wrong = 0    
input("Press enter to start")
print("--------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1 
end_time = time.time()
total_time = round(end_time - start_time , 1)

print("--------------------")
print("Nice work! You finished in",total_time,"seconds!")
print("Number of wrong attemps = ",wrong)