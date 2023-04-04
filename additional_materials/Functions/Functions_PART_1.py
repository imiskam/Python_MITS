"""
Тема функции.
https://docs.python.org/3/library/functions.html
- встроенные функции Python

https://docs.python.org/3/tutorial/controlflow.html#defining-functions
оф. документация по функциям
"""

""" 
Небольшой опрос:
1. Какая функция отвечает за вывод значений в терминал? - print()
2. Обязательны ли скобки для вызова функции? - обязательны, len(), print()
3. Какая функция отвечает за подсчет количества объектов в коллекции? - len()
4. Какая функция отвечает за вывод уникального идентификатора объекта? - id()
5. Какая функция отвечает за приведение к типу данных строка? - str()
6. Какой вывод будет у функции print(bool(True))? - 1

Ответив на эти простые вопросы можно смело делать вывод о том, что
функции созданы для того, чтобы как можно сильнее упростить работу с кодом. 

Функция в Python — это объект, принимающий аргументы и возвращающий значение.
С функциями мы неоднократно сталкивались.
"""


# рассмотрим пример создания пустой функции:
# def - является обязательным словом, обозначающим объявление функции
# def (define) - объявить
def example():
    pass  # оператор, который обозначает пропуск действия


"""
простыми словами, мы сделали функцию, 
которая при вызове ничего не делает. 
"""
