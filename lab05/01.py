import re
with open('row.txt', 'r', encoding='utf-8') as f:
    b = f.read()

a = re.findall(r'\b[a-z]+_[a-z]+\b', b)

with open('output1.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(a))

