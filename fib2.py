def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


number = int(input('How many numbers of Fibonacci sequence you want? '))
print('Fibonacci sequance:')
for i in range(1, number + 1):
    print('{:<3}{:>10}'.format(i, fib(i - 1)))
#'{0:*^}'.format(fib(i - 1))