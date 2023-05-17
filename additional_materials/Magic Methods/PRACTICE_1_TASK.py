class FileObject:

    def __init__(self, filename):
        self.file = open(filename, 'r+', encoding='UTF-8')

    def read_file(self):
        print(self.file.readlines())

    def __del__(self):
        print('__del__ сработал')
        self.file.close()
        del self.file


new_obj = FileObject('examp1.txt')
del new_obj
new_obj = FileObject('examp1.txt')
new_obj.read_file()
new_obj = 2
print(new_obj > 2)
