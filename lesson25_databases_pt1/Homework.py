# Домашнее задание
# Создать 2 таблицы в Базе Данных.
# Одна будет хранить текстовые данные (1 колонка). Другая числовые (1 колонка)
# Есть список, состоящий из чисел и слов.
# Если элемент списка слово, записать его в соответствующую таблицу,
# затем посчитать длину слова и записать её в числовую таблицу
# Если элемент списка число: проверить, если число чётное, записать его в таблицу чисел,
# если нечётное, то записать во вторую таблицу слово: «нечётное».
# Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. Если меньше,
# то обновить 1 запись в первой таблице на «hello»

import sqlite3

conn = sqlite3.connect("homework.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS homework_table_1
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 col_1 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS homework_table_2
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 col_1 INTEGER)""")

list_ = [1, 2, 3, 4, "hello", "world", 5, 6]

for i in list_:
    if type(i) == str:
        cursor.execute("INSERT INTO homework_table_1(col_1) VALUES (?)", (i,))
        cursor.execute("INSERT INTO homework_table_2(col_1) VALUES (?)", (len(i),))

    elif type(i) == int:
        if i % 2 == 0:
            cursor.execute("INSERT INTO homework_table_2(col_1) VALUES (?)", (i,))
        else:
            cursor.execute("INSERT INTO homework_table_1(col_1) VALUES (?)", ("нечётное",))
conn.commit()

cursor.execute("SELECT col_1 FROM homework_table_2")
rows = cursor.fetchall()
if len(rows) > 5:
    cursor.execute("DELETE FROM homework_table_1 WHERE id = 1")

elif len(rows) <= 5:
    cursor.execute("UPDATE homework_table_1 SET col_1 = 'hello' WHERE id = 1")

conn.commit()
cursor.execute("SELECT * FROM homework_table_1, homework_table_2")
print(cursor.fetchall())
