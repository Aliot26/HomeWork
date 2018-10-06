def lenght_list():
    N = int(input("Print lenght of list:"))
    if N > 20:
        print("Too large number")
    return N


def create_list():
    numbers = []
    for i in range(1, N + 1):
        new_number = int(input("Print number :"))
        numbers.append(new_number)
    return numbers


N = lenght_list()
numbers = create_list()
iterations = 1
while iterations < N:
    for j in range(N - iterations):
        if numbers[j] > numbers[j + 1]:
            (numbers[j], numbers[j + 1]) = numbers[j + 1], numbers[j]
    iterations += 1
print(numbers)
