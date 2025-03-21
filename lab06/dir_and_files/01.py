filename = '01.txt'

with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Amount of Rows: {len(lines)}")
