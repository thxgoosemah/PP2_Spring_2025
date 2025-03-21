def squaresToN(n):
    a = []
    for i in range(n + 1):
        a.append(i * i)
    return a
n = int(input(": "))
for square in squaresToN(n):
    print(square, end=" ")
