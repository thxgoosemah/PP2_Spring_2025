def divTo4and3(n):
    a = []
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            a.append(i)
    return a
n = int(input(": "))
for number in divTo4and3(n):
    print(number, end=" ")
