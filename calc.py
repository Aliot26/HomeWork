import math


def main():
    while True:
        x = inputNumber()
        op = inputOperation()
        y = inputNumber()
        answer = op(x, y)
        print("Answer : ", answer)


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


def inputNumber():
    while True:
        try:
            x = int(input('Enter a number (or a letter to exit):'))
            return x
        except ValueError:
            quit()


def inputOperation():
    opers = {'+': add, '-': sub, '*': mul, '/': div}
    expr = input('Enter an operation: ')
    if expr not in opers:
        print('Incorrect operation!')
        quit()
    return opers[expr]


main()
