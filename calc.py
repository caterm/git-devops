def calc(operation, first_number, second_number):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number
    elif operation == '^':
        return first_number ^ second_number

numberone = input('What is your first number?')
numberone = int(numberone)
numbertwo = input('What is your second number?')
numbertwo = int(numbertwo)
operator = input('What is your operation?')
calculation_result = calc(operator, numberone, numbertwo)
print(calculation_result)
