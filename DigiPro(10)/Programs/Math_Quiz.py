import random
import time

def welcome():
    '''Display game rules and welcome message and return player name'''
    print(f"{'*****MATH QUIZ*****' : ^65}")
    # prints a new line
    print(" ")
    name = input(f"{'Enter your name:' : >40}")
    print(" ")
    print(f'{name:>25}, Welcome to the Math quiz')
    print(" ")
    print(f"{'Game rules': ^65}")
    print(f"{'------------' : ^65}")
    print(f"{'* Quiz lasts for one minute *': ^65}")
    print(f"{'* Attempt as many questions as possible within the given time.*': ^65}")
    print(f"{'* Each correct answer carries one mark*' : ^65}")
    return name
def summary(name, q_no, correct, wrong, score):
    print(f'\n{name}, you have successfuly completed the quiz. Here are your results.')
    print(f"\n{'Questions attempted': ^21}{'Correct answers': ^18}{'Wrong answers': ^10}{'Total Score': ^15}")
    print(f'{"====================": ^21}{"=================": ^18}{"=============" : ^10}{"==========": ^15}')
    print(f'{q_no: ^21} {correct: ^18}{wrong: ^10}{score:^15}')
    
def calculate(number_1,number_2,operation):
    # perform the operation based on the operator
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        return 0

def generate_question():
    operators = ['+','-','*','/']
    # choose a random operator from a list of operators
    operation = random.choice(operators)
    # generate a random number between 1 and 10
    number_1 = random.randint(1,10)
    #generate a random number between 1 and 10
    number_2 = random.randint(1,10)
    # construct the question as a string
    question = f'{number_1} {operation} {number_2}'
    # evaluate the question and store the answer
    answer = calculate(number_1, number_2, operation)
    return question, answer
def start_quiz(name,duration):
    # set the score to 0
    score = 0
    #variable to count the number of questions, correct and wrong answers
    q_no = 0
    correct = 0
    wrong = 0
    # record the start time
    start_time = time.time()
    elapsed_time = 0
    # loop until the timer expires
    while elapsed_time < duration:
        # generate a random question
        q_no += 1
        question, correct_answer = generate_question()
        time_left = round(duration - (time.time()- start_time))
        print(f'Here is your question. You have {time_left} seconds left')
        # prompt the player to solve the question
        user_answer = float(input(f'{question} ='))
        user_answer = round(user_answer, 2)
        # check if the player's answer is correct
        if user_answer == correct_answer:
            print('Well done! That is the correct answer!')
            correct +=1
            score += 1
        else:
            wrong += 1
            print('Sorry! You entered a wrong answer.')
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # print the final score and summary
        summary(name, q_no, correct, wrong, score)
