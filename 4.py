import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec

# Создаем данные для sin(x), его производной и первообразной
x = np.linspace(0, np.pi, 1000)
sin_x = np.sin(x)
cos_x = np.cos(x)  # производная sin(x)
primitive = 1 - np.cos(x)  # первообразная sin(x)

# Создаем график с тремя панелями
fig = plt.figure(figsize=(15, 10))
gs = GridSpec(2, 2, figure=fig)

# Первая панель: sin(x), его производная и первообразная
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(x, sin_x, 'b-', linewidth=2, label='sin(x)')
ax1.plot(x, cos_x, 'r--', linewidth=2, label="cos(x) - производная sin(x)")
ax1.plot(x, primitive, 'g-.', linewidth=2, label="1-cos(x) - первообразная sin(x)")
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Функция sin(x), её производная и первообразная')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Читаем данные из CSV файлов
try:
    # Читаем CSV файлы с пробельным разделителем
    data_float = pd.read_csv('4_float.csv', sep='\s+', header=0)
    data_double = pd.read_csv('4_double.csv', sep='\s+', header=0)

    # Получаем названия колонок
    print("Колонки в float файле:", data_float.columns.tolist())
    print("Колонки в double файле:", data_double.columns.tolist())

    # Используем правильные названия колонок (берём первую и вторую колонку)
    n_float = data_float.iloc[:, 0].values  # первая колонка
    area_float = data_float.iloc[:, 1].values  # вторая колонка

    n_double = data_double.iloc[:, 0].values
    area_double = data_double.iloc[:, 1].values

    # Вторая панель: зависимость площади от количества точек
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.loglog(n_float, np.abs(area_float - 2.0), 'ro-', markersize=4, label='float', alpha=0.7)
    ax2.loglog(n_double, np.abs(area_double - 2.0), 'bo-', markersize=4, label='double', alpha=0.7)
    ax2.set_xlabel('Количество точек разбиения, n')
    ax2.set_ylabel('Абсолютная ошибка |S - 2|')
    ax2.set_title('Зависимость ошибки от количества точек')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Третья панель: значения интеграла
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.semilogx(n_float, area_float, 'ro-', markersize=4, label='float', alpha=0.7)
    ax3.semilogx(n_double, area_double, 'bo-', markersize=4, label='double', alpha=0.7)
    ax3.axhline(y=2.0, color='k', linestyle='--', label='Аналитическое значение = 2')
    ax3.set_xlabel('Количество точек разбиения, n')
    ax3.set_ylabel('Вычисленная площадь')
    ax3.set_title('Сходимость метода прямоугольников')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

except FileNotFoundError:
    print("CSV файлы 4_float.csv и 4_double.csv не найдены!")
    print("Создайте их сначала с помощью C++ программы")
except Exception as e:
    print(f"Ошибка при чтении CSV файлов: {e}")
    # Покажем первые строки файлов для отладки
    try:
        with open('4_float.csv', 'r') as f:
            print("Первые 3 строки 4_float.csv:")
            for i, line in enumerate(f):
                print(f"Строка {i}: {line.strip()}")
                if i >= 2:
                    break
    except:
        pass
plt.savefig("Графики 4 задание")
plt.tight_layout()
plt.show()
