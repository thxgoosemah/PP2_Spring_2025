import re

def match_a_anything_b(text):
    pattern = r'a.*b'
    return re.fullmatch(pattern, text) is not None

# Тестовые примеры
examples = ["ab", "axb", "a123b", "a____b", "ba", "a123", "xyzb", "acb"]
for e in examples:
    print(f"{e}: {match_a_anything_b(e)}")
