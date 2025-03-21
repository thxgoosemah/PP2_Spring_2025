import re
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
matches = re.findall(r'\b[a-z]+_[a-z]+\b', text)
print(": ", matches)

with open('output1.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(matches))

