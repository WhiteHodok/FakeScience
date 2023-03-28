import pandas as pd
from keras.models import Sequential
from keras.layers import Dense

# Загружаем данные из Excel-файла в DataFrame
df = pd.read_excel('ta.xlsx', sheet_name='table')

# Заполняем пустые значения нулями
df = df.fillna(0)

# Заменяем строковые значения на булевы
df = df.replace({'Да': 1, 'Нет': 0})

# Заменяем названия животных на числовые коды
df['who'] = df['who'].replace({
    'Кот': 0,
    'Собака': 1,
    'Попугай': 2,
    'Хомяк': 3,
    'Рыбка': 4,
    'Другие': 5
})

# Определяем входные и выходные данные для обучения
X = df[['have', 'who']].values
y = df['amount'].values

# Создаем модель нейросети
model = Sequential()
model.add(Dense(12, input_dim=2, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Компилируем модель
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Обучаем модель на данных
model.fit(X, y, epochs=100, batch_size=10)

# Получаем ввод от пользователя
have_pet = input("Есть ли у Вас домашнее животное? (да/нет): ").lower() == 'да'
if have_pet:
    pet = input("Какое у Вас домашнее животное? (кот/собака/попугай/хомяк/рыбка/другое): ").lower()
    pet_code = {
        'кот': 0,
        'собака': 1,
        'попугай': 2,
        'хомяк': 3,
        'рыбка': 4,
        'другое': 5
    }.get(pet, 5)
else:
    pet_code = 5

# Предсказываем вероятность долга в следующей сессии
probability = model.predict([[have_pet, pet_code]])[0][0]

if probability > 0.5:
    print("Вероятность наличия долга в следующей сессии: {:.2f}%".format(probability * 100))
else:
    print("Вероятность отсутствия долга в следующей сессии: {:.2f}%".format((1 - probability) * 100))
