# Задание 2
# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля. Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитайте среднее арифметическое всех элементов без учёта id.
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД.

import sqlite3
import random

conn = sqlite3.connect("task2_database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task2_table
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   col_1 INTEGER,
                   col_2 INTEGER)""")

for i in range(5):
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)
    cursor.execute("INSERT INTO task2_table (col_1, col_2) VALUES (?, ?)", (num_1, num_2))
conn.commit()

cursor.execute("SELECT col_1, col_2 FROM task2_table")
print(cursor.fetchall())

cursor.execute("SELECT AVG(col_1 + col_2) FROM task2_table")
average = cursor.fetchone()[0] / 2
print(f"Среднее значение: {average}")

if average > cursor.execute("SELECT COUNT(*) FROM task2_table").fetchone()[0]:
    cursor.execute("DELETE FROM task2_table WHERE id = 4")
    conn.commit()
    print("Четвертая запись удалена")
    cursor.execute("SELECT col_1, col_2 FROM task2_table")
    print(cursor.fetchall())