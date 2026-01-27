# While loop example
i = 1
while i <= 5:
    print(i)
    i += 1


# While loop with break
i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1


# While loop with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


# For loop example
for x in range(5):
    print(x)


# For loop with break
for x in range(10):
    if x == 6:
        break
    print(x)


# For loop with continue
for x in range(6):
    if x == 3:
        continue
    print(x)
