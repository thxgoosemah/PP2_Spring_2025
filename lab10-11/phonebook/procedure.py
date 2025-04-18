import psycopg2

conn = psycopg2.connect(
    dbname="PhoneBook",
    user="postgres",
    password="Johhny@",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def add_or_update_manual():
    name = input("name: ")
    phone = input("phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("User added or updated.")

def add_many():
    n = int(input("how many users neet to add: "))
    names = []
    phones = []
    for _ in range(n):
        names.append(input("name: "))
        phones.append(input("phone: "))
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    incorrect = cur.fetchone()[0] # получаем список неправильных данных
    conn.commit()
    if incorrect:
        print("incorrect data:", incorrect)
    else:
        print("added.")

def search_pattern():
    pattern = input("part of name or phone: ")
    cur.execute("SELECT * FROM find_by_pattern(%s)", (pattern,))
    results = cur.fetchall()
    for row in results:
        print(row)

def show_paginated():
    limit = int(input("set a limit: "))
    offset = int(input("enter a offset: "))
    cur.execute("SELECT * FROM get_users_with_pagination(%s, %s)", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_user_func():
    data = input("enter name or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (data,))
    conn.commit()
    print("deleted")

def menu():
    while True:
        print("1 add or update user")
        print("2 add many users")
        print("3 find by pattern")
        print("4 show paginated users")
        print("5 delete user")
        print("0 exit")

        cmd = input(": ")

        if cmd == "1":
            add_or_update_manual()
        elif cmd == "2":
            add_many()
        elif cmd == "3":
            search_pattern()
        elif cmd == "4":
            show_paginated()
        elif cmd == "5":
            delete_user_func()
        elif cmd == "0":
            break
        else:
            print("error")

    cur.close()
    conn.close()

menu()
