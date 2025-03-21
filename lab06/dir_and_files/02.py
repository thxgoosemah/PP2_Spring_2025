my_list = ['Apple', 'Banana', 'AK-47', 'M4A4']

with open('02.txt', 'w', encoding='utf-8') as f:
    for item in my_list:
        f.write(item + '\n')  
