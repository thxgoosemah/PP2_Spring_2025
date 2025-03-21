import re 
with open('row.txt', 'r', encoding='utf-8') as f:
    a = f.read().strip()
    
b= re.findall(r'\b[А-ЯA-Z][а-яa-z]*\b', a)

with open('output2.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(b))
