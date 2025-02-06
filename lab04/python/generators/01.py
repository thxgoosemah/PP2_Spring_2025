def squares_to_n(n):
    for i in range(n+1):
        yield i ** 2

n = int(input(": "))
for square in squares_to_n(n):
    print(square, end=" ")
