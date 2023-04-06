import json

# Домашнее задание

# Задача 1
# Пользователь будет вводить название и стоимость каждой своей покупки за день, до тех пор пока он не напишет “стоп”.
# Ваша задача записать это в json файл в формате:
# {"название" : "яблоко",
# "стоимость": "200"}

purchases = []

while True:
    item_name = input("Введите название товара (для остановки программы введите 'стоп'): ")
    if item_name.lower() == "стоп" or item_name.lower() == "stop":
        print("Программа остановлена")
        break
    item_price = float(input("Введите цену товара: "))
    purchase = {"название": item_name, "стоимость": item_price}
    purchases.append(purchase)

with open("purchases.json", "w", encoding="utf-8") as json_file_to_write:
    json.dump(purchases, json_file_to_write, indent=2, ensure_ascii=False)

# Задача 2
# Прочитать файл из предыдущего задания и вывести стоимость всех покупок за день

with open("purchases.json", "r", encoding="utf-8") as json_file_to_read:
    purchases = json.load(json_file_to_read)
    total_cost = 0
    for purchase in purchases:
        total_cost += purchase['стоимость']
    print(f"Cтоимость всех покупок: {total_cost}")
