import psycopg2  # импортируем psycopg2 для работы с базой данных

# подключаемся к базе данных
conn = psycopg2.connect(
    dbname="PhoneBook",  # название базы данных
    user="postgres",  # имя пользователя
    password="Johhny@",  # пароль пользователя
    host="localhost",  # хост, на котором работает база
    port="5432"  # порт подключения
)
cur = conn.cursor()  # создаём курсор для работы с базой

# функция для добавления или обновления пользователя вручную
def add_or_update_manual():
    name = input("name: ")  # спрашиваем имя
    phone = input("phone: ")  # спрашиваем номер телефона
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))  # вызываем процедуру добавления или обновления
    conn.commit()  # сохраняем изменения в базе
    print("User added or updated.")  # говорим пользователю, что все ок

# функция для добавления сразу нескольких пользователей
def add_many():
    n = int(input("how many users need to add: "))  # сколько пользователей добавляем
    names = []  # список для имен
    phones = []  # список для номеров телефонов
    for _ in range(n):  # циклим, пока все пользователи не добавятся
        names.append(input("name: "))  # добавляем имя
        phones.append(input("phone: "))  # добавляем номер телефона
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))  # вызываем процедуру для массового добавления
    incorrect = cur.fetchone()[0]  # получаем неверные данные, если они есть
    conn.commit()  # сохраняем изменения
    if incorrect:  # если есть неправильные данные
        print("incorrect data:", incorrect)  # выводим их
    else:  # если все правильно
        print("added.")  # говорим, что все добавлено

# функция для поиска по шаблону
def search_pattern():
    pattern = input("part of name or phone: ").strip()  # убираем пробелы в начале и конце
    query = "SELECT * FROM find_by_pattern(%s)"  # создаём запрос с параметром
    cur.execute(query, (pattern,))  # выполняем запрос с переданным параметром
    results = cur.fetchall()  # получаем все записи
    for row in results:  # выводим найденные записи
        print(row)

# функция для вывода пользователей с пагинацией
def show_paginated():
    limit = int(input("set a limit: "))  # сколько записей выводить за раз
    offset = int(input("enter a offset: "))  # с какого номера начать
    cur.execute("SELECT * FROM get_users_with_pagination(%s, %s)", (limit, offset))  # выполняем запрос с пагинацией
    results = cur.fetchall()  # получаем результаты
    for row in results:  # выводим результаты
        print(row)

# функция для удаления пользователя
def delete_user_func():
    data = input("enter name or phone to delete: ")  # спрашиваем, что удаляем: имя или телефон
    cur.execute("CALL delete_user(%s)", (data,))  # вызываем процедуру удаления
    conn.commit()  # сохраняем изменения в базе
    print("deleted")  # говорим, что удалено

# основное меню программы
def menu():
    while True:  # бесконечный цикл для меню
        print("1 add or update user")  # пункт для добавления или обновления
        print("2 add many users")  # пункт для добавления нескольких пользователей
        print("3 find by pattern")  # пункт для поиска по шаблону
        print("4 show paginated users")  # пункт для отображения пользователей с пагинацией
        print("5 delete user")  # пункт для удаления пользователя
        print("0 exit")  # пункт для выхода

        cmd = input(": ")  # спрашиваем, какую команду выполняем

        if cmd == "1":  # если выбрана команда для добавления/обновления пользователя
            add_or_update_manual()  # вызываем функцию для добавления или обновления
        elif cmd == "2":  # если выбрана команда для добавления нескольких пользователей
            add_many()  # вызываем функцию для массового добавления
        elif cmd == "3":  # если выбрана команда для поиска по шаблону
            search_pattern()  # вызываем функцию поиска
        elif cmd == "4":  # если выбрана команда для вывода с пагинацией
            show_paginated()  # вызываем функцию для пагинации
        elif cmd == "5":  # если выбрана команда для удаления
            delete_user_func()  # вызываем функцию для удаления пользователя
        elif cmd == "0":  # если выбрана команда для выхода
            break  # выходим из цикла
        else:  # если введена неправильная команда
            print("error")  # сообщаем, что команда неверная

    cur.close()  # закрываем курсор
    conn.close()  # закрываем соединение с базой

menu()  # запускаем меню
