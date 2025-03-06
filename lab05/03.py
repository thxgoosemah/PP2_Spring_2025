import re

def find_lowercase_with_underscore(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    return re.findall(pattern, text)

# Тестовые примеры
example_text = "hello_world some_text test_value HelloWorld test_123 _start_end_"
print(find_lowercase_with_underscore(example_text))
