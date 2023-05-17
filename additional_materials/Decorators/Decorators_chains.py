from datetime import datetime

"""
Декораторы можно объединять в цепочки, указывая при этом
порядок их применения  
"""


def chain(func):
    def wrapper():
        print('Функция начала работу')
        result = func()  # [1,2,3]
        print('Функция окончила работу')
        return result

    return wrapper


def count_the_time(func):  # создаем декоратор
    def wrapper():
        start = datetime.now()
        result = func()  # ([3,6,9], [1, 2, 3, 4, 5, 6, 7, 8])
        print(datetime.now() - start)
        return result

    return wrapper


@chain
@count_the_time
def create_list():
    list_ = []
    for _ in range(10 ** 5):
        if _ % 2 == 0:
            list_.append(_)
    return list_


@chain
@count_the_time
def create_list_gen():
    list_ = [i for i in range(10 ** 5) if i % 2 == 0]
    return list_


ex1 = create_list()
ex2 = create_list_gen()
