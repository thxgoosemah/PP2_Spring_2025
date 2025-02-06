class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

length = float(input(": "))
s = Square(length)
print("Square Area:", s.area())
