import pandas as pd
import numpy as np

'''
Dataframe — это табличная структура данных, напоминающая таблицы из Microsoft Excel. Ее главная задача — позволить 
использовать многомерные Series. Dataframe состоит из упорядоченной коллекции колонок, каждая из которых содержит
значение разных типов (числовое, строковое, булевое и так далее).
Dataframe можно воспринимать как словарь (dict), состоящий из Series, где ключи — названия колонок, 
а значения — объекты Series, которые формируют колонки самого объекта Dataframe. 
Наконец, все элементы в каждом объекте Series связаны в соответствии с массивом меток, называемым index.
'''

'''
Простейший способ создания Dataframe — передать объект dict в конструктор DataFrame(). 
Объект dict содержит ключ для каждой колонки, которую требуется определить, а также массив значений для них.

Если объект dict содержит больше данных, чем требуется, можно сделать выборку. 
Для этого в конструкторе Dataframe нужно определить последовательность колонок с помощью параметра column. 
Колонки будут созданы в заданном порядке вне зависимости от того, как они расположены в объекте dict.
'''

data = {'color': ['blue', 'green', 'yellow', 'red', 'white'],
        'objct': ['ball', 'pen', 'pencil', 'paper', 'mug'],
        'price': [12.0, 1.2, 74.9, 0.9, 1.7]}
frame = pd.DataFrame(data)
print(f'print(frame):\n{frame}\n')

# Для переименования колонки используется метод .rename
frame.rename(columns={'objct': 'object'}, inplace=True)
print(f'метод .rename():\n{frame}\n')

'''
Также для объектов Dataframe если метки явно не заданы в массиве index, pandas автоматически присваивает числовую
последовательность, начиная с нуля.
Вместо использования объекта dict можно определить три аргумента в конструкторе в следующем порядке: 
матрицу данных, массив значений для параметра index и массив с названиями колонок для параметра columns.
Колонке с индексами вы также можете дать название следующей командой:
'''
frame.columns.name = 'Ind'
print(f'Index named column:\n{frame}\n')

# frame.rename_axis("Ind", axis='columns', inplace=True)

'''
В большинстве случаев простейший способ создать матрицу значений — использовать np.arrange(16).reshape((4,4)). 
Это формирует матрицу размером 4х4 из чисел от 0 до 15.
'''
frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),
                      index=['red', 'blue', 'yellow', 'white'],
                      columns=['ball', 'pen', 'pencil', 'paper'])
print(f'frame2:\n{frame2}\n')

print(f'print(frame.columns):\n{frame.columns}\n')
print(f'print(frame2.columns):\n{frame2.columns}\n')
print(f'print(frame.index):\n{frame.index}\n')
print(f'print(frame2.index):\n{frame2.index}\n')

print(f'print(frame.values):\n{frame.values}\n')
print(f'print(frame2.values):\n{frame2.values}\n')

# Указав в квадратных скобках название колонки, можно получить значения в ней.
print(f"print(frame['price']):\n{frame['price']}\n")

# Возвращаемое значение — объект Series.
var = frame['price']
print(f"type(var):\n{type(var)}\n")

# Название колонки можно использовать и в качестве атрибута.
print(f"print(frame.price):\n{frame.price}\n")

# Для строк внутри Dataframe используется атрибут loc со значением индекса нужной строки.
print(f"print(frame.loc[3]):\n{frame.loc[3]}\n")

'''
Возвращаемый объект — это снова Series, где названия колонок — это уже метки массива индексов, 
а значения — данные Series.
Для выбора нескольких строк можно указать массив с их последовательностью.
'''
print(f"print(frame.loc[[2, 4]]):\n{frame.loc[[2, 4]]}\n")

'''
Если необходимо извлечь часть Dataframe с конкретными строками, то можно использовать номера индексов. 
Будут выведены данные из соответствующей строки и названия колонок.
'''
print(f"print(frame[0:1]):\n{frame[0:1]}\n")
print(f"print(frame[1:3]):\n{frame[1:3]}\n")

'''
Наконец, если необходимо получить одно значение из объекта, сперва нужно указать название колонки, 
а потом — индекс или метку строки.
'''
print(f"print(frame['object'][3]):\n{frame['object'][3]}\n")
