# вариант 1 - с пустой строкой
str_ = input("Введите строку: ")
sym = input("Введите символ: ")
str_without_sym = ""
for i in str_:
    if i != sym:
        str_without_sym += i
print(str_without_sym)

# вариант 2 - с пропуском симфола (pass)
str_ = input("Введите строку: ")
sym = input("Введите символ: ")
for i in str_:
    if i == sym:
        pass
    else:
        print(i, end="")

# вариант 3 - если символ не равен введенному, выводим i
string_ = input("Введите строку: ")
symbol = input("Введите символ: ")
for i in string_:
    if i != symbol:
        print(i, end="")
