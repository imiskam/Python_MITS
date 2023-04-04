list_ = ["мясо", "котлеты", "свекла", "морковь", "вареники"]
not_preferable_food = input("Введите блюдо, которое вы не употребляете: ")
for i in list_:
    if i == not_preferable_food:
        print("Я не ем", i)
        break
