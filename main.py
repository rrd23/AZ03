import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True, alpha=0.3)

# Добавление вертикальной линии для среднего значения
plt.axvline(mean, color='red', linestyle='dashed', linewidth=2, label=f'Среднее ({mean})')

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()