def main():
    N = lenghtList()
    numbers = createList(N)
    print(sorting(N, numbers))


def lenghtList():
    while True:
        try:
            N = int(input("Print lenght of list:"))
            return N
        except ValueError:
            print("Incorrect unput")


def createList(N):
    numbers = []
    for i in range(1, N + 1):
        try:
            newNumber = int(input("Print number :"))
        except ValueError:
            print("Incorrect unput")
        numbers.append(newNumber)
    return numbers


def sorting(N, numbers):
    iterations = 1
    while iterations < N:
        for j in range(N - iterations):
            if numbers[j] > numbers[j + 1]:
                (numbers[j], numbers[j + 1]) = numbers[j + 1], numbers[j]
        iterations += 1
    return numbers


main()