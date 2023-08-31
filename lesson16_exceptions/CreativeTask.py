import io


def read_file(file):
    try:
        with open(file, 'r') as file:
            file_info = file.read()
            return file_info
    except FileNotFoundError:
        print("Файл не существует или перемещен в другую директорию")
    # другой вариант
    # else:
    #     return file_info


def write_to_file(file, user_data):
    try:
        with open(file, 'w') as file:
            file.write(user_data)
    except io.UnsupportedOperation:
        print("Проверьте режим открытия файла!")
    except FileNotFoundError:
        print("Файл не существует или перемещен в другую директорию")


def main():
    file = "new_file.txt"
    user_data = input("Введите данные, чтобы записать в файл: ")
    write_to_file(file, user_data)
    print(read_file(file))  # для отладки


if __name__ == "__main__":
    main()
