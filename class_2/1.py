import numpy as np
import matplotlib.pyplot as plt

# Количество точек
N = 5

# Вектор координат x для образов С1
x1 = np.random.random(N)
# Вектор координат y для образов С1
x2 = x1 + np.random.random(N)
C1 = [x1, x2]

# Вектор координат x для образов С2
x1 = np.random.random(N)
# Вектор координат y для образов С2
x2 = x1 - np.random.random(N)
C2 = [x1, x2]

# Веса для разделения образов линейной функции где x = y
w = np.array([-0.3, 0.3])

for i in range(N):
    # Берем все образы относящиеся к C2
    x = np.array([C2[0][i], C2[1][i]])
    # Сумма всех вессов нейронна
    y = np.dot(w, x)

    # Активационная функция
    if y >= 0:
        print("Класс C1")
    else:
        print("Класс C2")


# Создает все образы с1 и с2 на графике
plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')

x = [0, 1]
y = [0, 1]
# Проводит линию от точки (0, 0) к точке (1, 1)
plt.plot(x, y)
plt.grid(True)
plt.show()
