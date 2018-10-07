def convertr(number):
    check(number)
    rnumber = ''
    rdict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    revkeys = rdict.keys()

    for intKey in revkeys:
        while number >= intKey:
            rnumber += rdict[intKey]
            number -= intKey
    return rnumber


def check(number):
    if number > 4000 or number < 0:
        print("Incorrect number")
        quit()


number = int(input("Write number less then 4000 : "))

print(convertr(number))