def main():
    number = inputNumbersFibonacci()
    print('Fibonacci sequance:')
    for i in range(1, number + 1):
        print('{:<3}{:>10}'.format(i, fib(i - 1)))


def inputNumbersFibonacci():
    while True:
        try:
            number = int(
                input('How many numbers of Fibonacci sequence you want? '))
            return number
        except ValueError:
            print("Incorrect input!")


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


main()
#try
