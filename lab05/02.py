import re

def match_a_followed_by_2to3_b(text):
    pattern = r'a{1}b{2,3}'
    return re.fullmatch(pattern, text) is not None

# Тестовые примеры
examples = ["abb", "abbb", "a", "abbbb", "ab", "abc"]
for e in examples:
    print(f"{e}: {match_a_followed_by_2to3_b(e)}")
