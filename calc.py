import math


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y == 0:
        print('Division by zero!')
        quit()
    return x / y


while True:
    try:
        x = int(input('Enter a number (or a letter to exit):'))
    except ValueError:
        quit()

    opers = {'+': add, '-': sub, '*': mul, '/': div}

    expr = input('Enter an operation: ')

    if expr not in opers:
        print('Incorrect operation!')
        quit()

    try:
        y = int(input('Enter a number (or a letter to exit):'))
    except ValueError:
        quit()

    print(opers[expr](x, y), '\n')
