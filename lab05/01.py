import re

# Читаем содержимое файла
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Ищем последовательности строчных букв, соединённых подчёркиванием
matches = re.findall(r'\b[a-z]+_[a-z]+\b', text)

# Выводим найденные последовательности
print("Найдено:", matches)

# Записываем результат в output.txt
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(matches))

