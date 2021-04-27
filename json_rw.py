# методы:
# json.load(text) - считывает файл в формате JSON и возвращает объекты python (превращает текст в json)
# json.loads(text) - считывает строку в формате JSON и возвращает объекты python
# json.dump(info, file) - записывает объект python в файл в формате JSON (записывает словарь info в json файл
# (файл надо заранее открыть))
# json.dumps() - возвращает строку в формате JSON

import json

with open("sample.json", "r") as read_file:
    data = json.load(read_file)

json.dump(data, open('copy.json', 'x'))
