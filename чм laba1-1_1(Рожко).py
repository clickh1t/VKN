import math

x1 = 88  # Точне число sqrt(x1)
x2 = 18 / 7  # Точне число x2
x1_1 = 9.38  # Наближене число x1
x2_2 = 2.57  # Наближене число x2


def f(x1, x1_1, x2, x2_2):
    rel_error_x1 = abs(math.sqrt(x1) - x1_1) / abs(math.sqrt(x1))
    rel_error_x2 = abs(x2 - x2_2) / abs(x2)

    if rel_error_x1 < rel_error_x2:
        print("Перша рівність точніше з відносною похибкою:", rel_error_x1)
    elif rel_error_x2 < rel_error_x1:
        print("Друга рівність точніше з відносною похибкою:", rel_error_x2)
    else:
        print("Обидві рівності мають однакову точність з відносною похибкою:", rel_error_x1)


f(x1, x1_1, x2, x2_2)
