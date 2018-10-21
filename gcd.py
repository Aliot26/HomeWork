def main():
    numberA = inputNumber()
    numberB = inputNumber()
    gcd(numberA, numberB)


def inputNumber():
    while True:
        try:
            a = abs(int(input('Enter a number: ')))
            return a
        except ValueError:
            print("Incorrect input!")


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    gcd = a + b
    print(gcd)


main()
