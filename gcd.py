a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
gcd = a + b
print(gcd)