import time
import math

num = int(input("Введите число: "))
delay = int(input("Задержка (мс): "))

time.sleep(delay / 1000)
print("Корень числа:", math.sqrt(num))
