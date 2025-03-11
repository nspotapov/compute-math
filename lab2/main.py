import numpy as np
from pyparsing import alphas


def point_info(x, f):
    return f'x = {x}, f(x) = {f(x)}'


def hooke_jeeves(f, x0, delta0, epsilon, alpha):
    x = np.array(x0)
    delta = np.array(delta0)

    iteration = 0

    while np.linalg.norm(delta) > epsilon:
        iteration += 1

        print()
        print('=' * 40)
        print('Итерация', iteration)

        print('Текущая базовая точка', point_info(x, f))

        sample_x = exploratory_search(f, x, delta)

        if f(sample_x) < f(x):
            print('Исследующий поиск УДАЧНЫЙ')

            x_p = sample_search(f, x, sample_x)

            if f(x_p) < f(x):
                print('Поиск по образцу УДАЧНЫЙ')
                x = x_p
            else:
                print('Поиск по образцу ПРОВАЛЕН')
                x = sample_x

            print()
            print('Новая базовая точка', point_info(x, func))

        else:
            print('Исследующий поиск ПРОВАЛЕН')

            print('Уменьшаем шаг', delta, '->', delta / alpha)
            delta = delta / alpha
            print('ε =', np.linalg.norm(delta))

    return x, f(x)


def exploratory_search(f, x, delta):
    print()
    print('Выполняем исследующий поиск')

    x_new = np.array(x)
    f_x_new = f(x_new)

    for i in range(len(x)):
        x_up = x_new.copy()
        x_down = x_new.copy()

        x_up[i] += delta[i]
        x_down[i] -= delta[i]

        f_x_up = f(x_up)
        f_x_down = f(x_down)

        if (f_x_up < f_x_new and f_x_up < f_x_down):
            x_new = x_up
            f_x_new = f_x_up
        elif (f_x_down < f_x_new):
            x_new = x_down
            f_x_new = f_x_down

    if (any([x_new[i] != x[i] for i in range(len(x))])):
        print('Найдена точка', x_new, func(x_new))
    return x_new


def sample_search(f, x1, x2):
    print()
    print('Выполняем поиск по образцу')
    while f(x2) < f(x1):
        x2, x1 = x2 + (x2 - x1), x2
    print('Найдена точка', x2, f(x2))
    return x2


def func(x):
    return x[0] ** 2 + 2 * x[1] ** 2 + 5 * x[2] ** 2 - 2 * x[0] * x[1] - 4 * x[0] * x[2] - 2 * x[2]
    # return 8 * (x[0] ** 2) + 4 * x[0] * x[1] + 5 * (x[1] ** 2)


# x0 = [-4, -4]
# delta0 = [1, 1]

x0 = [1, 0, 0]
delta0 = [1e+6, 1e+6, 1e+6]

alpha = 2
epsilon = 1e-4

x, val = hooke_jeeves(func, x0, delta0, epsilon, alpha)

print()
print("Точка экстремумв:", x)
print("Минимальное значение функции:", val)
