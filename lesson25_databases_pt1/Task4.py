# Задание 4
# Создайте метод класса для работы с БД
# В БД
# Если передан 1 аргумент, вставить в таблицу запись с числом 3
# Если переданы 2 аргумента: проверить или второй аргумент является числом.
# Если условие верно, то удалить первую запись с БД.
# Если переданы 2 аргумента, их значения неизвестны, а 3 является числом, то обновить на число 77 запись 3.

import sqlite3

conn = sqlite3.connect("task4_database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS task4_table
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 col_1 INTEGER)""")

cursor.execute("SELECT * FROM task4_table")


class Database:
    def add_to_database(self, arg_1=None, arg_2=None, arg_3=None):
        if arg_1 is not None and arg_2 is None and arg_3 is None:
            cursor.execute("INSERT INTO task4_table(col_1) VALUES (3)")
            conn.commit()
        elif arg_1 is not None and arg_2 is not None and arg_3 is None:
            if type(arg_2) is int:
                cursor.execute("DELETE FROM task4_table WHERE id = 1")
                conn.commit()
        elif arg_1 is not None and arg_2 is not None and type(arg_3) is int:
            cursor.execute("UPDATE task4_table SET col_1 = 77 WHERE id = 3")
            conn.commit()


database = Database()
database.add_to_database("1", "1", 1)
cursor.execute("SELECT * FROM task4_table")
print(cursor.fetchall())

conn.close()