import numpy as np

# Визначимо функцію, для якої ми шукаємо корені
def equation(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Похідна функції
def derivative(x):
    return 4*x**3 + 6*x**2 + 4*x + 6

# Початкова наближена точка
x0 = 1.0
epsilon = 1e-6  # Точність

# Максимальна кількість ітерацій (захист від зациклення)
max_iterations = 1000

for i in range(max_iterations):
    f_x0 = equation(x0)
    f_prime_x0 = derivative(x0)
    
    if abs(f_prime_x0) < epsilon:
        break
    
    x1 = x0 - f_x0 / f_prime_x0
    
    if abs(x1 - x0) < epsilon:
        break
    
    x0 = x1

print(f"Корінь рівняння: {x0}")
