import time
import math

num = int(input(": "))
delay = int(input("ms: "))

time.sleep(delay / 1000)
print("square root:", math.sqrt(num))
