import sympy as sp

# Спершу визначимо символьну змінну
x = sp.symbols('x')

# Задаємо рівняння
equation = x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Знайдемо корені аналітично
analytical_roots = sp.solve(equation, x)

# Далі, визначимо функцію f(x), яку потрібно буде диференціювати для методу хорд
def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Тепер реалізуємо метод половинного ділення
def bisection_method(func, a, b, tol):
    while (b - a) / 2.0 > tol:
        midpoint = (a + b) / 2.0
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint
    return (a + b) / 2.0

# Визначимо початковий інтервал для методу половинного ділення
a = -2
b = 2

# Визначимо точність
tolerance = 0.0001

# Знайдемо корінь методом половинного ділення
bisection_result = bisection_method(f, a, b, tolerance)

# Далі, реалізуємо метод хорд
def secant_method(func, x0, x1, tol):
    while abs(func(x1)) > tol:
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        x0, x1 = x1, x2
    return x1

# Визначимо початкові точки для методу хорд
x0 = -2
x1 = 2

# Знайдемо корінь методом хорд
secant_result = secant_method(f, x0, x1, tolerance)

# Виведемо результати
print("Аналітичні корені:", analytical_roots)
print("Корінь методом половинного ділення:", bisection_result)
print("Корінь методом хорд:", secant_result)
