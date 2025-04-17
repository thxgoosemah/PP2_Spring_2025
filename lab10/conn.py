import psycopg2

conn = psycopg2.connect(
    dbname="PhoneBook",
    user="postgres",
    password="Johhny@",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")

conn.commit()
print("Таблица создана!")
cur.close()
conn.close()