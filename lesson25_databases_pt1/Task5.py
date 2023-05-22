# Задание 5
# Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки.
# Первая – id, вторая и третья - с данными.

import sqlite3

conn = sqlite3.connect("task5_database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task5_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 col_1 TEXT,
                 col_2 TEXT)""")

for row in range(3):
    cursor.execute("INSERT INTO task5_table(col_1, col_2) VALUES (?, ?)", ("word1", "word2"))
conn.commit()

cursor.execute("SELECT * FROM task5_table")
print(cursor.fetchall())

cursor.execute("DELETE FROM task5_table WHERE id = 2")
cursor.execute("UPDATE task5_table SET col_1 = 'hello', col_2 = 'world' WHERE id=3")

cursor.execute("SELECT * FROM task5_table")
print(cursor.fetchall())

with open("task5_database.txt", "w", encoding="UTF-8") as file:
    for row in cursor.execute("SELECT * FROM task5_table"):
        file.write(f"{row[0]}\t{row[1]}\t{row[2]}\n")