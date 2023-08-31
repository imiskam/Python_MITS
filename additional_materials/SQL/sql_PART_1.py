import sqlite3  # импортируем соответствующий модуль

# подключаемся к базе данных
# при этом, если БД с таким именем будет отсутствовать
# она создастся автоматически
conn = sqlite3.connect('name.db')

# инициализируем курсор
cursor = conn.cursor()

# теперь создаем таблицу
# 1. Создаем таблицу, если таковая отсутствует
# 2. Указываем название таблицы
# 3. Указываем поле id - по нему будут настраиваться связи между таблицами
# 4. Колонки col_1 и col_2 будут текстовыми
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS
        tab_1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        col_1 TEXT,
        col_2 TEXT
    )
    ''')

# теперь заполняем нашу таблицу
# 1. Указываем конструкцию INSERT INTO (вставить в <название таблицы>)
# 2. Указываем в какие поля будем вставлять данные.
# 3. Указываем конструкцию VALUES со вставляемыми значениями
cursor.execute('''
    INSERT INTO tab_1(col_1, col_2)
    VALUES('hello','world')
''')
# ОБЯЗАТЕЛЬНО СОХРАНЯЕМ ИЗМЕНЕНИЯ
conn.commit()

# Заполнение таблицы с помощью данных, получаемых из переменных (или значений функций, например)
# пример:

cursor.execute("""
    CREATE TABLE IF NOT EXISTS 
    tab_2(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        col_1 TEXT, 
        col_2 TEXT
    )
""")

# Снова обращаемся к курсору
# показываем ему, в какую таблицу обращаемся
# указываем колонки
# после указываем значения, при этом необходимо указать спец. символ ?
# после чего после указания базовой конструкции, после запятой
# Указываем какие значения необходимо поместить (а точнее наши переменные)

var1 = "red"
var2 = "black"

cursor.execute(""" 
    INSERT INTO tab_2(col_1, col_2) 
    VALUES(?,?)
""", (var1, var2))

data_list = [('yellow', 'white') for x in range(10)]

command = """ 
    INSERT INTO tab_2(col_1, col_2) 
    VALUES(?,?)
"""

for tuple_ in data_list:
    cursor.execute(command, tuple_)

# Снова сохраняем
conn.commit()

# Теперь, давайте достанем из нашей таблицы tab_1 отправленные туда значения
# обращаемся к курсору
# вызываем метод Execute и для него указываем соответствующую команду
cursor.execute('''SELECT * FROM tab_2''')
# указываем команду на получение данных
print(cursor.fetchall())

"""
>>>>>>ЗАДАНИЕ: создайте 10 различных записей в таблицу tab_1
с клавиатуры
"""

#
#

for _ in range(10):
    col_1_inp = input('Введите значение для колонки col_1:')
    col_2_inp = input('Введите значение для колонки col_2: ')
    cursor.execute('''
        INSERT INTO tab_1(
            col_1,
            col_2)
        VALUES(?,?)
    ''', (col_1_inp, col_2_inp))

conn.commit()
