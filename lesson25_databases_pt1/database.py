import sqlite3

conn = sqlite3.connect("name.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)""")
cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES ("hello", "world")""")
conn.commit()

d = "red"
f = "black"
cursor.execute("""CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)""")
cursor.execute("""INSERT INTO tab_1(col_1, col_2) VALUES (?,?)""", (d, f))
conn.commit()

cursor.execute("""SELECT * FROM tab_1""")
print(cursor.fetchall())

#########################################################

cursor.execute("""CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)""")

data_list = [("yellow", "white") for x in range(10)]

command = """
    INSERT INTO tab_2(col_1, col_2)
    VALUES(?,?)
"""

for tuple_ in data_list:
    cursor.execute(command, tuple_)

conn.commit()

cursor.execute("""SELECT * FROM tab_2""")
print(cursor.fetchall())