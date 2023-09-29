import math

x1 = 88  # Точне число sqrt(x1)
x2 = 18 / 7  # Точне число x2
x1_1 = 9.38  # Наближене число x1
x2_2 = 2.57  # Наближене число x2


def f(x1, x1_1, x2, x2_2):

    err_x1_abs = abs(math.sqrt(x1) - x1_1)
    err_x2_abs = abs(x2 - x2_2)

    rel_error_x1 = err_x1_abs / abs(math.sqrt(x1))
    rel_error_x2 = err_x2_abs / abs(x2)

    is_x1_close = math.isclose(
        math.sqrt(x1), x1_1, rel_tol=rel_error_x1, abs_tol=err_x1_abs)
    is_x2_close = math.isclose(
        x2, x2_2, rel_tol=rel_error_x2, abs_tol=rel_error_x2)

    if is_x1_close and is_x2_close:
        print("Обидві рівності точні з однаковою точністю")
    elif is_x1_close:
        print("Перша рівність точніше")
    elif is_x2_close:
        print("Друга рівність точніше")
    else:
        print("Обидві рівності неточні")


f(x1, x1_1, x2, x2_2)
