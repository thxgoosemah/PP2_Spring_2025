class StringHandler:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input(": ")

    def printString(self):
        print(self.text.upper())

s = StringHandler()
s.getString()
s.printString()