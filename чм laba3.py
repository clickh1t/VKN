import numpy as np
from scipy.optimize import newton

# Визначимо функцію, для якої ми шукаємо корені
def equation(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Початкова наближена точка
initial_guess = 1.0

# Використовуємо метод Ньютона для знаходження кореня
root = newton(equation, initial_guess)

print(f"Корінь рівняння: {root}")
