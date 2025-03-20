import re  # Импортируем модуль регулярных выражений

# Открываем файл 'row.txt' для чтения и читаем содержимое
with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read().strip()

# С помощью регулярного выражения добавляем пробел перед каждой заглавной буквой
# r'([A-Z])' — находит каждую заглавную букву
# r' \1' — заменяет её на пробел + та же заглавная буква
result = re.sub(r'([A-Z])', r' \1', text).strip()

# Открываем (или создаём) файл 'output4.txt' для записи результата
with open('output4.txt', 'w', encoding='utf-8') as f:
    # Записываем результат в файл
    f.write(result)
