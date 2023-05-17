from datetime import datetime

"""
Рассмотрим еще одну ситуацию, при которой уже сам декоратор будет принимать аргументы.
Для этого нам придется сделать еще одну обертку.
"""


def count_the_time(arg):
    """
    задаем блок инструкций для работы с аргументами из декоратора
    """
    print(f"{arg} - аргумент декоратора count_of_time")

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer


@count_the_time('arg')
def create_list_gen(k):
    list_ = [i for i in range(k) if i % 2 == 0]
    return list_


# ex1 = create_list_gen(15)

"""
Рассмотрим подробнее как это работает.
Декораторы могут быть использованы для разных ситуаций. Как пример
реализация логирования, работа с URL-ами, редиректами и прочим, что может
встретиться в Django, да и в целом в ЯП Python. 
"""

ex1 = count_the_time('arg')(create_list_gen)(123123123)
