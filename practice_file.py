import json


# Задача 1
# функция выводит содержимое файла
def read_entire_file(path2file):
    text = open(path2file, 'r').read()
    print(text)


# read_entire_file('sample.txt')


# Задача 2
# функция выводит первые n строк файла
def read_first_n_lines(path2file, n):
    with open(path2file, 'r') as f:
        text = f.readlines()
    for _ in range(n):
        print(text.pop(0).strip())


# read_first_n_lines('sample.txt', 2)


# Задача 3
# функция добавляет в конец файла новую строку с текстом END OF FILE
def add_end_to_file(path2file, end='\nEND OF FILE'):
    with open(path2file, 'a') as f:
        f.write(end)

# add_end_to_file('sample.txt')


# Задача 4
# функция возвращает список из строк файла
def text2list(path2file):
    with open(path2file, 'r') as f:
        lst_text = f.readlines()
    return lst_text


# print(text2list('sample.txt'))


# Задача 5
# функция возвращает самую длинную строку файла
def longest_line(path2file):
    with open(path2file, 'r') as f:
        lst_text = f.readlines()
    longest = lst_text[0]
    for string in lst_text[1:]:
        if len(string) > len(longest):
            longest = string
    return longest


# print(longest_line('sample.txt'))


# Задача 6
# функция дописывает в конец файла пустую строку, строку Количество слов в тексте: x
# и строку Количество различных слов в тексте: y
# где x - количество слов в файле, y - количество уликальных слов в файле
def add_info_to_file(path2file):
    with open(path2file, 'r') as f:
        text = f.read()
    sentences = text.split('.')
    words = []
    for sentence in sentences:
        words.extend(sentence.split())
    word_count = len(words)
    diff_word_count = len(set(words))

    with open(path2file, 'a') as f:
        f.write('\n')
        f.write(f'\nКоличество слов в тексте: {word_count}')
        f.write(f'\nКоличество различных слов в тексте: {diff_word_count}')


# add_info_to_file('sample.txt')


# Задача 7
# фуекция фозвращает список имен из json файла
def get_names_from_json(path2file):
    with open(path2file, "r") as read_file:
        data = json.load(read_file).keys()
    return data


# print(*get_names_from_json('sample.json'))


# Задача 8
# функция создает json файл, оценки в котором заменены на цифры
def convert_marks(path2file):
    with open(path2file, "r") as read_file:
        data = json.load(read_file)
        marks_dict = {'A': 5, 'B': 4, 'C': 3, 'D': 2}
    for el in data:
        temp_makr = data.get(el)
        data[el] = marks_dict.get(temp_makr)
    json.dump(data, open('digit_marks.json', 'x'))


# convert_marks('sample.json')
