def change_num(a, b):
    a, b = b, a


numbers = [1, 2, 56, 32, 51, 2, 8, 92, 15]
print(numbers)
N = len(numbers)
iterations = 1

while iterations < N:
    for j in range(N - iterations):
        if numbers[j] > numbers[j + 1]:
            change_num(numbers[j], numbers[j + 1])
    iterations += 1
print(numbers)
