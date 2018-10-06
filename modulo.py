nl = []
for x in range(100, 999):
    if (x % 7 == 0) or (x % 9 == 0):
        nl.append(str(x))

for y in nl[0:25]:
    print(y)
