def fibonacci(max):
    a, b = 1, 1
    while a < max:
        yield a
        a, b = b, a + b


for n in fibonacci(20):
    print(n)
