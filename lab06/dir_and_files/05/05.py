import os

file_path = 'die.txt'

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK): 
        os.remove(file_path)
        print("ok.")
    else:
        print("not found")
else:
    print("err")
