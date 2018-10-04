def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print('Fibonacci sequance:')
for i in range(1, 31):
    print(i, '. ', fib(i - 1))
