import re

with open('row.txt', 'r', encoding='utf-8') as f:
    a = f.read()

b = re.sub(r'[ ,.]', ':', a)

with open('output4.txt', 'w', encoding='utf-8') as f:
    f.write(b)
