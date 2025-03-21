s = "Hello World! Python is good"

upper_count = 0
lower_count = 0

for char in s:
    if char.isupper():
        upper_count += 1
    if char.islower():
        lower_count += 1

print("U:", upper_count)
print("L:", lower_count)
