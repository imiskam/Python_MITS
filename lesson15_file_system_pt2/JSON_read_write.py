import json

# Преобразуем json-строку в словарь
str_ = '{"id": "4538", "email": "test1@mail.com", "name": "John", "surname": "Doe", "driver license": "true"}'
data = json.loads(str_)
print(data["id"])
print(data["driver license"])

# Читаем json-данные из файла и преобразуем в словарь
with open("user_info.json", encoding="utf-8") as json_file:
    data = json.load(json_file)
print(data["email"])

# Преобразуем словарь в json-строку
data = {"id": 898, "email": "test1@mail.com", "name": "Митя", "surname": "Митропавлов", "driver license": True}
str_ = json.dumps(data)
print(str_)
# Без юникода
str_ = json.dumps(data, ensure_ascii=False)
print(str_)
# Преобразуем словарь в json и записываем в файл
with open("user_info2.json", "w", encoding="utf-8") as json_file2:
    json.dump(data, json_file2, ensure_ascii=False)
