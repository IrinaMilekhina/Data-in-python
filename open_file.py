# 'r' открытие на чтение (значение по умолчанию)
# 'w' открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x' открытие на запись, если файла не существует, иначе исключение
# 'a' открытие на дозапись, информация добавляется в конец файла
# 'b' открытие в бинарном режиме (например, документы Word и Excel бинарные)
# 't' открытие в тектовом режиме (значение по умолчанию)
# 'r+' открытие на дозапись, изначально смотрим на начало файла

import json

with open("sample.json", "r") as read_file:
    data = json.load(read_file)

my_file = open('sample.txt', 'r').readlines()
print(my_file[0])
