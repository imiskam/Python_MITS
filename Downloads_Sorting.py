import os
import shutil

# Создаем словарь с расширениями файлов и соответствующими папками назначения
extensions = {
    '.txt': 'Text Files',
    '.pdf': 'PDF Files',
    '.jpg': 'Image Files',
    '.png': 'Image Files',
    '.mp3': 'Music Files',
    '.mp4': 'Video Files',
    '.zip': 'Archive Files'
}

# Путь к папке Downloads
downloads_folder = os.path.expanduser('~/Downloads')

# Итерируемся по всем файлам в папке Downloads
for filename in os.listdir(downloads_folder):
    # Получаем полный путь к файлу
    filepath = os.path.join(downloads_folder, filename)

    # Проверяем, является ли файл файлом (а не папкой)
    if os.path.isfile(filepath):
        # Получаем расширение файла
        extension = os.path.splitext(filename)[1]

        # Проверяем, есть ли это расширение в нашем словаре
        if extension in extensions:
            # Получаем имя папки назначения для этого расширения
            folder_name = extensions[extension]

            # Создаем папку назначения, если ее еще нет
            folder_path = os.path.join(downloads_folder, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Перемещаем файл в папку назначения
            destination_path = os.path.join(folder_path, filename)
            shutil.move(filepath, destination_path)

            print(f'Moved {filename} to {folder_name}')