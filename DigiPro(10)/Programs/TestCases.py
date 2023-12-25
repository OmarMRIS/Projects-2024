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