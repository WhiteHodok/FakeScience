import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




# Загрузка данных из Excel-файла в DataFrame
df = pd.read_excel('ta.xlsx', sheet_name='table')

df = df.fillna(0)

df = df.replace({'Да': True, 'Нет': False})

df['who'] = df['who'].replace({
    'Кот': 'Cat',
    'Собака': 'Dog',
    'Попугай': 'Parrot',
    'Хомяк': 'Hamster',
    'Рыбка': 'Fish',
    'Другие': 'Other'
})


# Вывод данных DataFrame
#print(df.head())

# Заменяем значения в столбце "who" на более понятные
#df['who'] = df['who'].replace({0: 'No pets', 1: 'Has pets'})

# Заменяем значения в столбце "animal" на более понятные
#df['animal'] = df['animal'].replace(
    #{'Cat': 'Кот', 'Dog': 'Собака', 'Parrot': 'Попугай', 'Hamster': 'Хомяк', 'Fish': 'Рыбка', 'Other': 'Другие'})

# Преобразуем значения в столбце 'who' в тип category
#df['who'] = pd.Categorical(df['who'])

# Разбиваем данные на две группы: с домашними животными и без
#with_pets = df[df['who'] != 0]
#without_pets = df[df['who'] == 0]

# Строим график
#sns.displot(data=with_pets, x='amount', hue='who', kind='kde', fill=True, palette=['green', 'red', 'blue', 'purple', 'orange'])
#sns.displot(data=without_pets, x='amount', hue='who', kind='kde', fill=True, palette=['yellow'])

#plt.show()
#df['have'] = df['have'].replace({'Да': 1, 'Нет': 0})

#sns.lmplot(x='have', y='amount', data=df)
#plt.show()

#corr = df['have'].corr(df['amount'])
#print(f"Коэффициент корреляции: {corr}")



