def main():
    modulo(25)


def modulo(num):
    nl = []
    for x in range(100, 999):
        if (x % 7 == 0) or (x % 9 == 0):
            nl.append(str(x))
            if len(nl) <= num:
                print(x)


main()