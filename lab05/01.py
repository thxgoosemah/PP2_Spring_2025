import re

def match_a_followed_by_b(text):
    pattern = r'a*b*'
    return re.fullmatch(pattern, text) is not None

# Тестовые примеры
examples = ["a", "ab", "abb", "abbb", "ba", "b", "abc"]
for e in examples:
    print(f"{e}: {match_a_followed_by_b(e)}")
