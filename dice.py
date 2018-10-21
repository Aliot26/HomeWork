import random


def main():
    at = "Attacker: "
    de = "Defender: "
    units = inputUnits()
    attakerDice = dice(units[0])
    defenderDice = dice(units[1])
    print("")
    print("Dice:")
    atDice = printDice(attakerDice)
    deDice = printDice(defenderDice)
    print(at, atDice)
    print(de, deDice)
    print("")
    print("Outcome:")
    res = outcomeLost(attakerDice, defenderDice)
    printOutcome(res, at, de)


def printOutcome(res, at, de):
    if res[0] == 1:
        print("  ", at, "Lost ", res[0], " unit")
    else:
        print("  ", at, "Lost ", res[0], " units")
    if res[1] == 1:
        print("  ", de, "Lost ", res[1], " unit")
    else:
        print("  ", de, "Lost ", res[1], " units")


def outcomeLost(attakerDice, defenderDice):
    a = list(sortingList(attakerDice))
    d = list(sortingList(defenderDice))
    dLost = 0
    aLost = 0
    if len(a) > len(d):
        lenght = len(d)
    else:
        lenght = len(a)
    for i in range(lenght):
        if a[i] > d[i]:
            dLost += 1
        else:
            aLost += 1

    return aLost, dLost


def sortingList(l):
    l = reversed(sorted(l))
    return l


def printDice(d):
    d = sortingList(d)
    r = "-".join(map(str, d))
    return r


def dice(v):
    i = 0
    listDice = list()
    while i < v:
        k = random.randrange(1, 6)
        listDice.append(k)
        i += 1
    return listDice


def inputUnits():
    try:
        countA = int(input("How many units attack? "))
    except ValueError:
        print("Incorrect input!")
    try:
        countD = int(input("How many units defend? "))
    except ValueError:
        print("Incorrect input!")
    return countA, countD


main()
