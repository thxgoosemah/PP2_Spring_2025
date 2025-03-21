import re 

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read().strip()
result = re.sub(r'([A-ZА-ЯЁ])', r' \1', text).strip()

with open('output3.txt', 'w', encoding='utf-8') as f:
    f.write(result)
