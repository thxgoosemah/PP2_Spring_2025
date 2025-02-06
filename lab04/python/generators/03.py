def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

# Example usage:
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
for square in squares(a, b):
    print(square, end=" ")
