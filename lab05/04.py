import re

def find_uppercase_followed_by_lowercase(text):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, text)

# Тестовые примеры
example_text = "Hello World Python Programming hello HELLO hELLo PyThoN"
print(find_uppercase_followed_by_lowercase(example_text))
