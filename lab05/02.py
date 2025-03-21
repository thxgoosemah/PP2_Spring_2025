import re 
with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read().strip()
    
result = re.findall(r'\b[А-ЯA-Z][а-яa-z]*\b', text)

with open('output2.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(result))
