import pandas as pd

titanic = pd.read_csv('titanic.csv', delimiter=',', encoding='utf-8')
# Данные представлены в виде таблицы. Посмотрим на первые 5 строк
print(f"Посмотрим на первые 5 строк:\n{titanic.head()}\n")

# Посчитайте общие статистикм по числовым данным с помощью метода describe
print(f"Статистики:\n{titanic.describe()}\n")

# А теперь давайте отсортируем данные по возрастанию цены в столбце Fare
print(f"Сортировка:\n{titanic.sort_values('Fare')}\n")

# Давайте создадаим новый признак на основе старого, новый признак будет называться
# age_category и определяться следующим образом
# 0 если возраст меньше 18
# 1 если от 18 до 30 (18 включается, а 30 нет)
# 2 если от 30 до 50 (30 включается, а 50 нет)
# 3 если старше 50


def age_category(age):
    if 0 < age < 18:
        res = 0
    elif age < 30:
        res = 1
    elif age < 50:
        res = 2
    elif age >= 50:
        res = 3
    else:
        res = age

    return res


age_categories = [age_category(el) for el in titanic['Age']]  # создайте список из стоблца и примените к нему функцию,
titanic['age_category'] = age_categories

print(f"Новый признак age_category:\n {titanic.head(7)}\n")
# Сколько мужчин / женщин находилось на борту?

count_sex = titanic.groupby('Sex').count()[['PassengerId']].reset_index().to_string(index=False)
print(f"Количество мужчин и женщин на борту:\n{count_sex}\n")

# Правда ли, что люди моложе 30 лет выживали чаще, чем люди старше 50 лет? Посчитайте
# число выживших в обеих группах и общее число людей в этих группах?

count_age_category_survived = titanic.groupby(['Survived', 'age_category']).count()[['PassengerId']]
survived_in_30 = count_age_category_survived['PassengerId'][1][1]
not_survived_in_30 = count_age_category_survived['PassengerId'][0][1]
survived_in_50 = count_age_category_survived['PassengerId'][1][3]
not_survived_in_50 = count_age_category_survived['PassengerId'][0][3]

print(f"Всего людей в группе моложе 30 лет: "
      f"{survived_in_30 + not_survived_in_30}\n"
      f"Из них выжило: {survived_in_30}, "
      f"не выжило: {not_survived_in_30}\n"
      f"Процент выживших: {int(survived_in_30/(survived_in_30 + not_survived_in_30)*100)}%\n"
      f"\nВсего людей в группе старше 50 лет: "
      f"{survived_in_50 + not_survived_in_50}\n"
      f"Из них выжило: {survived_in_50}, "
      f"не выжило: {not_survived_in_50}\n"
      f"Процент выживших: {int(survived_in_50/(survived_in_50 + not_survived_in_50)*100)}%\n")

# Сохраните файл в csv с тем именем, которое ему выберете

titanic.to_csv('titanic_done.csv', index=False, sep=';')