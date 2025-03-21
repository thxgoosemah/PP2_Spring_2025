import re 

with open('row.txt', 'r', encoding='utf-8') as f:
    c_str = f.read().strip()  

s_str = re.sub(r'([A-ZА-ЯЁ])', r'_\1', c_str).lower()

with open('output5.txt', 'w', encoding='utf-8') as f:
    f.write(s_str)
