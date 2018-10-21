inputS = ("The greatest victory is that which requires no battle")


def reverseString(inputString):
    inputString = inputString.split()
    inputString = inputString[-1::-1]
    output = " ".join(inputString)
    return output


print("The greatest victory is that which requires no battle")
print(reverseString(inputS))
