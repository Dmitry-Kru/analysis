import pandas as pd
# Словарь для df
data = {
    'Ученик': ['Ученик1', 'Ученик2', 'Ученик3', 'Ученик4', 'Ученик5', 'Ученик6', 'Ученик7', 'Ученик8', 'Ученик9', 'Ученик10'],
    'Математика': [4, 5, 3, 4, 5, 3, 4, 5, 4, 3],
    'Информатика': [5, 4, 5, 3, 4, 5, 3, 4, 5, 4],
    'Физика': [3, 4, 5, 4, 3, 4, 5, 3, 4, 5],
    'Русский язык': [4, 3, 4, 5, 4, 3, 4, 5, 3, 4],
    'Английский язык': [5, 4, 3, 4, 5, 4, 3, 4, 5, 4]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

# Среднее
mean_grades = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_grades)

# Медиана
median_grades = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_grades)

# Q1 и Q3 для оценок по математике
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("IQR для оценок по математике:", IQR_math)

# Вычисляем стандартное отклонение по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)