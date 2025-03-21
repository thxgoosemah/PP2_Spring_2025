import os

file = 'die.txt'

if os.path.exists(file):
    if os.access(file, os.W_OK): 
        os.remove(file)
        print("ok.")
    else:
        print("not found")
else:
    print("err")
