class Something:

    # переопределяем метод __new__, в котором обязательно делаем ссылку
    # на текущий класс, также указываем на приём неограниченного количества
    # позиционных и ключевых аргументов
    def __new__(cls, *args, **kwargs):
        # выведем сообщение о том, что наш метод __new__ сработал
        print(f'сработал __new__ для класса: {cls.__name__}')

        # теперь мы, к примеру, решили на этапе создания объекта добавить
        # новый атрибут, для этого мы переопределяем __new__ родителя (object)
        instance = super().__new__(cls)

        # добавляя к экземпляру новый атрибут
        instance.new_attribute = 'добавлено'

        # в результате работы функции мы должны вернуть адрес нашего нового объекта
        # в нашем случае он будет определен в instance
        return instance


example = Something()
print(example.__dir__())