class File:#Определяем базовый класс File
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'File: {self.name}'
class ReadFile(File):#Дочерний класс, наследующий File, для файлов только для чтения
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f'ReadFile: {self.name}'
class WriteFile(File):#Дочерний класс, наследующий File, для файлов только для записи
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f'WriteFile: {self.name}'
class ReadWriteFile(ReadFile, WriteFile):#Дочерний класс, наследующий и ReadFile, и WriteFile, для файлов для чтения и записи
    def __init__(self, name):
        super().__init__(name)
    def __str__(self):
        return f'ReadWriteFile: {self.name}'
#Создаем экземпляры каждого класса и выводим информацию о каждом из них
file1 = File("example.txt")
print(file1)
read_file1 = ReadFile("readme.txt")
print(read_file1)
write_file1 = WriteFile("notes.txt")
print(write_file1)
read_write_file1 = ReadWriteFile("data.txt")
print(read_write_file1)