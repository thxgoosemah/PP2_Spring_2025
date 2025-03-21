import re

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()

result = re.sub(r'[ ,.]', ':', text)

with open('output4.txt', 'w', encoding='utf-8') as f:
    f.write(result)
