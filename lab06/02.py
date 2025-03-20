s = "Hello World! Python Is Awesome"

upper_count = 0
lower_count = 0

for char in s:
    if char.isupper():
        upper_count += 1
    if char.islower():
        lower_count += 1

print("Верхний регистр:", upper_count)
print("Нижний регистр:", lower_count)
