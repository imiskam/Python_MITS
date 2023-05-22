from datetime import datetime

"""
Разбор декоратора начнем с постановки задачи, чтобы понять
с какой практической целью можно использовать данный
инструмент.
Так на предыдущих занятиях я говорил о том, что
работа генератора списков производится быстрее, 
чем создание списка через цикл.
В данном конкретном примере мы рассмотрим этот тезис
и убедимся (или разубедимся) в этом.
"""

"""
Для начала давайте поговорим о том, что же такое
Декоратор — это паттерн проектирования (design pattern) 
в Python, а также функция второго уровня, то есть 
принимающая другие функции в качестве переменных и возвращающая их.
Декораторы работают не только с функциями, но и с классами 
и методами
"""

"""
Сейчас давайте к нашим двум функциям напишем нашу функцию декоратор. 
"""


def count_the_time(func):  # создаем декоратор
    """
    param func: функция, которую мы будем оборачивать
    return: возвращает результат работы функции wrapper
    """
    def wrapper():  # создаем вложенную функцию-обертку
        start = datetime.now()  # отмечаем старт отсчета
        result = func()  # вызываем функцию, которая придет в качестве аргумента в count_the_time(func)
        print(datetime.now() - start)  # отмечаем время работы
        return result  # возвращаем результат переданной функции, т.е. то, что функция должна была вернуть

    return wrapper  # возвращаем то, что вернула функция wrapper


@count_the_time  # вызов декоратора для функции
def create_list():
    list_ = []
    for _ in range(10 ** 5):
        if _ % 2 == 0:
            list_.append(_)
    return list_


@count_the_time  # вызов декоратора для функции
def create_list_gen():
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]
    return list_


create_list()
create_list_gen()

"""
Таким нехитрым способом нам удалось избежать проблем с нарушением едва ли не основных
принципов проектирования и построения наших будущих программ. Декоратор - вещь важная и 
часто используемая. 
Вместе с тем, мы еще не рассмотрели добавление параметров в наши функции, а точнее
как и куда добавлять наши параметры в наш декоратор, чтобы мы могли работать
также и с аргументами наших функций. 
Decorator_PART_3
"""