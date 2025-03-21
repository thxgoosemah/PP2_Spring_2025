import re 

with open('row.txt', 'r', encoding='utf-8') as f:
    b = f.read().strip()
a = re.sub(r'([A-ZА-ЯЁ])', r' \1', b).strip()

with open('output3.txt', 'w', encoding='utf-8') as f:
    f.write(a)
