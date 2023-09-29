import math


def significant_figures_narrow(value, uncertainty):
    uncertainty_str = str(uncertainty)
    if 'e' in uncertainty_str:
        _, exponent = uncertainty_str.split('e')
        return len(str(int(value))) - int(exponent)
    else:
        return len(str(uncertainty).split('.')[1])


def significant_figures_wide(value, delta_percent):
    return -math.log10(delta_percent / 100)


value_a = 0.39642
uncertainty_a = 0.00022

value_b = 46.453
delta_percent_b = 0.15

significant_figures_narrow_a = significant_figures_narrow(
    value_a, uncertainty_a)
significant_figures_wide_b = significant_figures_wide(value_b, delta_percent_b)

print(
    f"а) Кількість правильних значущих цифр у вузькому розумінні: {significant_figures_narrow_a}")
print(
    f"б) Кількість правильних значущих цифр у широкому розумінні: {significant_figures_wide_b}")
