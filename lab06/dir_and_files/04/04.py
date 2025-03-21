a = 'text.txt'
b = 'text1.txt'

with open(a, 'r', encoding='utf-8') as src:
    content = src.read()

with open(b, 'w', encoding='utf-8') as dst:
    dst.write(content)

print("Uspeshno.")
