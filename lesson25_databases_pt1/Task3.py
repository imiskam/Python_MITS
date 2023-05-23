# Задание 3
# Создайте новую Базу данных. Поля: id, 2 целочисленных поля. Целочисленные поля заполняются рандомно от 0 до 9.
# Выберите случайную запись из БД.
# Если каждое число данной записи чётное, то удалите эту запись.
# Если нечётное, то обновите данные в ней на (2, 2)

import sqlite3
import random

conn = sqlite3.connect("task3_database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task3_table
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   col_1 INTEGER,
                   col_2 INTEGER)""")

for i in range(5):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    cursor.execute("INSERT INTO task3_table (col_1, col_2) VALUES (?, ?)", (num_1, num_2))
conn.commit()
cursor.execute("SELECT * FROM task3_table")
print("ДО:", cursor.fetchall())

random_id = random.randint(1, 5)
cursor.execute(f"SELECT col_1, col_2 FROM task3_table WHERE id = {random_id}")
row = cursor.fetchone()

if row[1] % 2 == 0 and row[2] % 2 == 0:
    cursor.execute(f"DELETE FROM task3_table WHERE id = {random_id}")
else:
    cursor.execute(f"UPDATE task3_table SET col_1 = {2}, col_2 = {2} WHERE id = {random_id}")
conn.commit()

cursor.execute("SELECT * FROM task3_table")
print("ПОСЛЕ:", cursor.fetchall())

conn.close()