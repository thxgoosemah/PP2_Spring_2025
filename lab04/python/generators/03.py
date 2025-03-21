def squares(a, b):
    a = []
    for i in range(a, b + 1):
        a.append(i * i)
    return a
a = int(input("a: "))
b = int(input("b: "))
for i in squares(a, b):
    print(i, end=" ")
