import numpy as np


def hooke_jeeves(func, x0, step_size=1, epsilon=1e-4, alpha=2):
    x = np.array(x0)
    fx = func(x)
    while step_size > epsilon:
        # Поиск по образцу
        new_x = exploratory_search(func, x, step_size)
        new_fx = func(new_x)

        if new_fx < fx:  # если улучшение
            # Формируем новое базисное решение
            x = new_x + (new_x - x)
            fx = func(x)
        else:  # уменьшаем шаг
            step_size /= alpha

        print(x, step_size)

    return x, fx


def exploratory_search(func, x, step_size):
    x_new = np.array(x)
    for i in range(len(x)):
        # Проба движения вперёд
        x_temp = x_new.copy()
        x_temp[i] += step_size
        if func(x_temp) < func(x_new):
            x_new = x_temp
        else:
            # Проба движения назад
            x_temp[i] -= 2 * step_size
            if func(x_temp) < func(x_new):
                x_new = x_temp
    return x_new


# Пример: минимизация квадратичной функции
def func(x):
    return x[0] ** 2 + 2 * x[1] ** 2 + 5 * x[2] ** 2 - 2 * x[0] * x[1] - 4 * x[0] * x[2] - 2 * x[2]


x0 = [1, 1, 1]

opt_x, opt_val = hooke_jeeves(func, x0)
print("Оптимальное значение переменных:", opt_x)
print("Минимальное значение функции:", opt_val)
