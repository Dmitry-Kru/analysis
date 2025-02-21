import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(50)  # Первый набор из 50 случайных чисел
y = np.random.rand(50)  # Второй набор из 50 случайных чисел

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.7, edgecolor='black')

# Добавление подписей и заголовка
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Диаграмма рассеяния для случайных данных')

# Включение сетки
plt.grid(True)

# Показ графика
plt.show()