str_ = input("Введите строку: ")
# задать предикат, где значение введенной строки с большой буквы будет сравниваться с "Mister"
is_mister = str_.capitalize() == "Mister"
if is_mister:
    print(is_mister)
else:
    print(False)
