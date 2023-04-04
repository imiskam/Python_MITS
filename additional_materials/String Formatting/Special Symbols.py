# Специальные символы строк

"""
При указании в строках специальных символов следует учитывать,
что при установлении таких символов прим. \n
такой символ вместе с обратным слэшем и n будет учитываться как
один символ в строке.
"""

my_string = "first word\nsecond word"
# \n - символ переноса на новую строку
print(my_string)

my_string = "\tfirst word second word"
# \t - символ горизонтальной табуляции
print(my_string)

my_string = 'first word\'s second word'
# \' - символ апострофа
print(my_string)

my_string = 'first word\b second word'
# \b - эмуляция клавиши backspace
# при использовании удалит предыдущий символ
print(my_string)

"""
Рассмотрим пример:
my_string = 'i need a dollar'
В момент создания нашей переменной мы решили, что
хотим заключить наше слово need в \ \ в  обратные слэши
my_string = 'i \need\ a dollar'
"""

my_string = 'i \need\ a dollar'
print(my_string)

"""
Как мы видим из результата, \n воспринялся
PyCharm-ом как спец символ и перенес часть нашей
строки на новую строку. Подобная ситуация может произойти
при записывании пути к нужному нам файлу
"C:\Program Files (x86)\hide.me VPN\Hide.me.exe"
Для решения данной проблемы мы должны разобрать понятие
экранирование или экранированные последовательности.

Экранированные последовательности – это последовательности символов, определяющие специальные символы,
которые тяжело ввести с клавиатуры или отобразить на экране. 
К таким символам можно отнести, например, символ новой строки, символ звукового сигнала PC Speaker, 
символ клавиши BackSpace и прочее.
"""

path = "C:\Program Files (x86)\tide.me VPN\Hide.me.exe"
print(path)

"""
Для исключения подобных ситуаций необходимо экранировать подобные символы.
Причем, визуально будет казаться, что мы указываем \\,
однако Python воспринимает подобные конструкции как один символ \
"""

path = "C:\\Program Files (x86)\\hide.me VPN\\Hide.me.exe"
print(path)

"""
Кроме того, подобные конструкции можно использовать к любым символам, которые
могут (или имеют) двойное назначение
пример:
"""

string_ = "Like a \"boss\""
print(string_)

"""
Также следует отметить, что в Python предусмотрены raw последовательности, или r-строка 
т.е. сырые последовательности, в которых все специальные символы в строке
игнорируются
"""

string_ = r"\n\n\t\n.ad.s./1/213.23..as/asd."
print(string_)

"""
Как мы видим из примера, все спец. символы, указанные в нашей строке
были проигнорированы, в связи с чем строка была записана в том виде
в котором мы ее задали. 
Как раз-таки подобную практику реализуют для установления путей к объектам
"""

path = r"C:\Program Files (x86)\tide.me VPN\Hide.me.exe"
print(path)
