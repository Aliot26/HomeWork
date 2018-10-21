def main():
    print('I am python')
    name = input('Who are you? ')
    if name == "":
        hello()
    else:
        hello(name)


def hello(name='world'):
    print("Hello, " + name)


main()