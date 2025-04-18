import psycopg2
import csv

# подключение к базе
conn = psycopg2.connect(
    dbname="PhoneBook",
    user="postgres",
    password="Johhny@",
    host="localhost",
    port="5432"
)
cur = conn.cursor() # создаём "курсор" — через него выполняются SQL-запросы

# создание самой таблицы если нету
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
""")
conn.commit() # сохраняем изменения в базе

# добавить файлы вручную
def add_manual():
    name = input("name: ")
    phone = input("phone: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone)) # добавляем в таблицу с именами и номерами
    conn.commit()
    print("+")

# загрузить данные из csv файла
def add_from_file():
    filename = input("choose csv file: ")
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row['name'], row['phone'])) # ищет из csv файла строку с name и row и заполняет таблицу
    conn.commit()
    print("loaded")

# обновление номера
def update():
    name = input("whose number need to update: ")
    new_phone = input("new number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name)) # Обнаваляет данные из номера для определнного имени 
    conn.commit()
    print("updated")

# нахождение контакта
def find():
    data = input("name or number: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f"%{data}%", f"%{data}%"))
    results = cur.fetchall() # получаем все найденные строки
    for row in results:
        print(row[1], row[2])
    if not results:
        print("nothing found")

# удалние контакта
def delete():
    data = input("delete name/number ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (data, data))
    conn.commit()
    print("deleted")

# меню выбора действий
def menu():
    while True:
        print("1 add")
        print("2 load from csv file")
        print("3 update number")
        print("4 find contact")
        print("5 delete contact")
        print("0 exit")

        cmd = input(": ")

        if cmd == "1":
            add_manual()
        elif cmd == "2":
            add_from_file()
        elif cmd == "3":
            update()
        elif cmd == "4":
            find()
        elif cmd == "5":
            delete()
        elif cmd == "0":
            break
        else:
            print("error")

    cur.close()
    conn.close()

menu()
