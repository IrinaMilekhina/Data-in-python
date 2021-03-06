import pandas as pd

# Создадим csv-файл для дальнейшей работы с ним:
data = {'furniture': ['chair', 'chair', 'chair', 'table', 'table', 'table', 'table', 'table', 'bed', 'bed', 'bed',
                      'bed', 'bed', 'bed', 'bed', 'sofa', 'sofa', 'sofa', 'sofa', 'cupboard', 'cupboard', 'cupboard'],
        'uniq_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016,
                    1017, 1018, 1019, 1020, 1021, 1022],
        'price': [1000, 600, 550, 300, 320, 330, 290, 310, 200, 220, 240, 230, 220, 100, 80, 420,
                    600, 500, 390, 410, 430, 410]}
frame = pd.DataFrame(data)

frame.to_csv('fur.csv', index=False)  # для изменения разделителя добавить параметр sep=';'

'''
Для анализа данных с помощью pandas, необходима структура данных, совместимая с pandas.
Информация может храниться в файлах .csv или таблицах SQL. Возможно, в файлах Excel. Или даже файлах. tsv.

С большей частью аналитических методов логичнее работать в двухмерной структуре,
поэтому мы будем использовать DataFrames.

pd.read_csv('fur.csv', delimiter=',', encoding='utf-8')
pd.read_xlsx('your_file.xlsx', delimiter=';', encoding='utf-8')
pd.read_csv('https://pythonru.com/downloads/fur.csv', delimiter=';')
для указания разделителя также можно использовать sep=';'

Но для дальнейшего обращения к данным нужно сохранить их в переменную
'''
article_read = pd.read_csv('fur.csv', delimiter=',', encoding='utf-8')
print('Методы\n')
print(f'.shape - количество строк и столбцов:\n{article_read.shape}\n')
print(f'.head() - вывод первых строк (по умолчанию 5):\n{article_read.head()}\n')
print(f".dropna().head() - не выводить пропущенные значения:\n"
      f"{article_read.dropna().head()}\n")
print(f'.tail() - вывод последних строк (по умолчанию 5):\n{article_read.tail()}\n')
print(f'.sample(5) - вывод случайных 5 строк (по умолчанию 1):\n{article_read.sample(5)}\n')

print(f"print(article_read[['furniture', 'uniq_id']] - для вывода только нужных колонок:"
      f"\n{article_read[['furniture', 'uniq_id']]}\n")

# ---------------------------------------------------------------------------------------------------------------------
'''
Фильтрация данных из DataFrame.
Предположим, что вы хотите сохранить только bed, которые представлены в источнике «furniture».
Для этого нужно отфильтровать по значению «bed» в колонке «furniture» .
Шаг 1) В первую очередь он оценивает каждую строчку в квадратных скобках: является ли 'bed' значением колонки fur.
Результат всегда будет булевым значением (True или False).
'''
print('Фильтрация\n')
print(f"article_read.furniture == 'cupboard':\n{article_read.furniture == 'cupboard'}\n")

'''
Шаг 2) Затем он выводит каждую строку со значением True из таблицы fur.
'''
print(f"article_read[article_read.furniture == 'cupboard']:\n{article_read[article_read.furniture == 'cupboard']}\n")

# ---------------------------------------------------------------------------------------------------------------------
'''
Агрегация данных — это процесс объединения различных строк из таблиц с помощью специальных функций, 
которые называются агрегаторами. 
Расчет различных статистических метрик (сумм,средних значений, значений счетчиков и медиан) 
выполняется с помощью агрегаторов. Агрегация позволяет сопоставлять данные из разных таблиц
Проще говоря агрегация — это процесс превращения значений набора данных в одно значение.

Для примера используем предыдущий csv файл содержащий информацию мебели (наименование, количество, стоимость).

Рассмотрим пять вариантов агрегации для этого файла
1.      Посчитать количество строк (количество наименований мебели).
2.      Посчитать общее кол-во мебели.
3.      Найти самую дешевую мебель и вывести значение price.
4.      И самую дорогую мебель и вывести значение price.
5.      Наконец, среднее price.
'''
print('Агрегация данных\n')

'''
1.Посчитать количество furniture — то же самое, что применить функцию count к набору данных furniture.
Функция count() считает количество значений в каждой колонке.
В случае с furniture есть 3 колонки, в каждой из которых по 22 значения.
'''
print(f".furniture.count():\n{article_read.furniture.count()}\n")

# 2. Следуя той же логике, можно с легкостью найти сумму значений в колонке price с помощью:
print(f".price.sum():\n{article_read.price.sum()}\n")

print(f"['furniture'].isnull().sum() - количество пропущенных значений в колонке:\n"
      f"{article_read['furniture'].isnull().sum()}\n")

# 3,4.Какое наименьшее значение в колонке price? Определить это несложно:
print(f".price.min():\n{article_read.price.min()}\n")

# То же и с максимальным значением:
print(f".price.max():\n{article_read.price.max()}\n")

# 5,6. Среднестатистические показатели, например среднее и медиана считаются:

print(f".price.mean():\n{article_read.price.mean()}\n")
print(f".price.median():\n{article_read.price.median()}\n")

# для вывода конкретных значений есть методы .isin([]) .between() .query('2 <= column_name < =4')
print(f"df[df['price'].isin([1000, 600]:\n{article_read[article_read['price'].isin([1000, 600])]}\n")
print(f"df[df['price'].between(80, 220)]:\n{article_read[article_read['price'].between(80, 220)]}\n")
print(f".query('80 <= price < =200'):\n{article_read.query('80 <= price < =200')}\n")

# метод .describe() сразу покажет основные статистические данные по колонкам с числовыми значениями фрейма
print(f".describe():\n{article_read.describe()}\n")

print(f'.furniture.unique() - вывод всех уникальных значений колонки:\n{article_read.furniture.unique()}\n')
print(f'.furniture.nunique() - вывод количества уникальных значений колонки:\n{article_read.furniture.nunique()}\n')
print(f"['furniture'].value_counts() - вывод количества по уникальным значениям колонки:\n"
      f"{article_read['furniture'].value_counts()}\n")

# ---------------------------------------------------------------------------------------------------------------------
'''
Группировка полей запроса позволяет получить информацию о подгруппах таблицы. Например, сгруппировав по коду заказа
данные в таблице, содержащей сведения о заказах, можно получить сведения об итоговой сумме по каждому заказу.

Между переменной article_read и функцией.mean() нужно вставить ключевое слово groupby:
'''
print('Агрегация данных\n')
print(f".groupby('furniture').mean():\n{article_read.groupby('furniture').mean()}\n")

'''
На выводе выше мы видим, что названия колонок начинают съезжать по разным строкам. 
Чтобы этого избежать необходимо использовать:
'''
print(f".groupby('furniture').mean().reset_index().to_string(index=False):\n"
      f"{article_read.groupby('furniture').mean().reset_index().to_string(index=False)}\n")

'''
Как и раньше, pandas автоматически проведет расчеты .mean() для оставшихся колонок (колонка furniture пропала, потому
что по ней проводилась группировка). Можно или игнорировать колонку uniq_id или удалить ее одним из следующих способов:
'''
var = article_read.groupby('furniture').mean()[['price']]  # возвращает объект DataFrame.
print(f"var = article_read.groupby('furniture').mean()[['price']]\nvar.reset_index().to_string(index=False):\n"
      f"{var.reset_index().to_string(index=False)}\n")

'''
Можно поменять метод агрегации с .mean() на любой изученный до этого, также можно производить группировку не только по
одному столбцу, но и по нескольким. Их также следует указывать в скобках, через запятую.
'''
