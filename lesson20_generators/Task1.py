types_list = [
    1,
    "строка",
    [1, 2, 3],
    {1, 2, 3},
    1.1,
    True,
    (1, 2, 3),
    frozenset({1, 2, 3}),
    {"key": "value"},
    range(1, 10)
]

for i in types_list:
    print(f"Тип данных: {type(i)}, "
          f"наличие __iter__: {'__iter__' in i.__dir__()}, "
          f"наличие __getitem__: {'__getitem__' in i.__dir__()}")
