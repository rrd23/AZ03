import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_points = 100
x_data = np.random.rand(num_points)
y_data = np.random.rand(num_points)

# Создание диаграммы рассеяния
plt.figure(figsize=(10, 8))
plt.scatter(x_data, y_data, alpha=0.6)

plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)

# Добавление линии y = x для сравнения
plt.plot([0, 1], [0, 1], color='red', linestyle='--', label='y = x')

# Настройка осей
plt.xlim(0, 1)
plt.ylim(0, 1)

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()

# Вывод первых 5 элементов каждого массива для проверки
print("Первые 5 элементов X:", x_data[:5])
print("Первые 5 элементов Y:", y_data[:5])