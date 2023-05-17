from datetime import datetime


def count_the_time(func):
    def wrapper(*args, **kwargs):
        """
        Для того, чтобы работать в т.ч. с аргументами, а также с именованными аргументами
        необходимо воспользоваться *args **kwargs. А с учетом того, что мы работаем
        с функцией, которая будет обрабатываться во вложенной функции wrapper,
        то и *args **kwargs необходимо подавать внутрь нее.
        """
        start = datetime.now()
        result = func(*args, **kwargs)
        # соответственно необходимо внести изменения и в вызове функции
        # вызываемой функции
        print(datetime.now() - start)
        return result

    return wrapper


@count_the_time
def create_list_gen(k):
    list_ = [i for i in range(k) if i % 2 == 0]
    return list_


ex1 = create_list_gen(123123123)

"""
Давайте рассмотрим, как в действительности работает наш декоратор @count_list_gen 
"""

example = count_the_time  # присвоим нашу функцию переменной example
"""
Вспоминаем, что при написании count_the_time() 
мы осуществим вызов функции, а нам необходимо получить ее функционал.

посмотрим на пример ниже.  
"""
example(create_list_gen)(1111111)
print(example(create_list_gen).__name__)
# example(create_list_gen) - возвращает нам результат работы функции wrapper
# example(create_list_gen)(15) можно представить как wrapper(15)

"""
Все это по сути делает сама инструкция использования декоратора
изнутри. 
Через символ @ мы указываем, какую функцию мы хотим обернуть.
"""