# Задание 1
# Создайте новую Базу данных. В ней создайте таблицу с тремя полями, два текстовых, одно – целое число.
# Число запрашивается с клавиатуры, а слова задаются статически. Выведите каждую запись в отдельную строку

import sqlite3

conn = sqlite3.connect("task1_database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task1_table
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   col_1 TEXT,
                   col_2 TEXT,
                   col_3 INTEGER)""")

word_1 = "синица"
word_2 = "журавль"
num = int(input("Введите число: "))

cursor.execute("INSERT INTO task1_table (col_1, col_2, col_3) VALUES (?, ?, ?)", (word_1, word_2, num))
conn.commit()

cursor.execute("SELECT * FROM task1_table")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print("\n".join(map(str, row)))

