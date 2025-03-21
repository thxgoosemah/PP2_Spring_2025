import re 

with open('row.txt', 'r', encoding='utf-8') as f:
    camel_str = f.read().strip()  

snake_str = re.sub(r'([A-ZА-ЯЁ])', r'_\1', camel_str).lower()

with open('output5.txt', 'w', encoding='utf-8') as f:
    f.write(snake_str)
