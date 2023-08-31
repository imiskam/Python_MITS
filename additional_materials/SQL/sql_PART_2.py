import sqlite3

conn = sqlite3.connect('name.db')
cursor = conn.cursor()

# теперь, давайте рассмотрим несколько примеров
# Выборки данных из нашей базы данных

# ВЫБЕРИ ВСЕ ЗНАЧЕНИЯ ИЗ КОЛОНКИ TAB_1, ГДЕ ИМЯ КОЛОНКИ HELLO
print('--------------------------------------------------------------------------------------------------------')
cursor.execute("""SELECT col_1 FROM tab_1 WHERE col_1 = 'hello' """)
conn.commit()
print(cursor.fetchall())
print()

print('--------------------------------------------------------------------------------------------------------')

# ВЫБЕРИ ВСЕ ЗНАЧЕНИЯ ИЗ КОЛОНКИ TAB_1 ОТСОРТИРОВАВ ПО КОЛОНКЕ COL_2
cursor.execute("""SELECT * FROM tab_1 ORDER BY id DESC """)
conn.commit()
print(cursor.fetchall())
print()

# ВЫБЕРИ ВСЕ ЗНАЧЕНИЯ ИЗ TAB_1 ГДЕ ПОЛЕ КОЛОНКИ БУДЕТ НАЧИНАТЬСЯ С 7
cursor.execute("""SELECT * FROM tab_1 WHERE col_2 LIKE '%orl%' """)
conn.commit()
s = cursor.fetchall()
print(s)
