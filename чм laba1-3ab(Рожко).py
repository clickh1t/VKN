import math


def narrow_error_limits(value):
    str_value = str(value)
    n = len(str_value)
    absolute_error_lower = 0.5 * 10 ** (-n)
    absolute_error_upper = 1.5 * 10 ** (-n)
    relative_error_lower = absolute_error_lower / value
    relative_error_upper = absolute_error_upper / value
    return (absolute_error_lower, absolute_error_upper), (relative_error_lower, relative_error_upper)


def wide_error_limits(value):
    str_value = str(value)
    n = len(str_value)
    absolute_error_lower = 0.5 * 10 ** (-n-1)
    absolute_error_upper = 0.5 * 10 ** (-n)
    relative_error_lower = absolute_error_lower / value
    relative_error_upper = absolute_error_upper / value
    return (absolute_error_lower, absolute_error_upper), (relative_error_lower, relative_error_upper)


value_a = 15.644
value_b = 6.125

narrow_error_limits_a = narrow_error_limits(value_a)
narrow_error_limits_b = narrow_error_limits(value_b)
wide_error_limits_a = wide_error_limits(value_a)
wide_error_limits_b = wide_error_limits(value_b)

print(
    f"а) Граничні абсолютні та відносні похибки у вузькому розумінні для числа {value_a}:")
print(
    f"   Абсолютна похибка: від {narrow_error_limits_a[0][0]} до {narrow_error_limits_a[0][1]}")
print(
    f"   Відносна похибка: від {narrow_error_limits_a[1][0]} до {narrow_error_limits_a[1][1]}")
print(
    f"б) Граничні абсолютні та відносні похибки у вузькому розумінні для числа {value_b}:")
print(
    f"   Абсолютна похибка: від {narrow_error_limits_b[0][0]} до {narrow_error_limits_b[0][1]}")
print(
    f"   Відносна похибка: від {narrow_error_limits_b[1][0]} до {narrow_error_limits_b[1][1]}")
print(
    f"а) Граничні абсолютні та відносні похибки у широкому розумінні для числа {value_a}:")
print(
    f"   Абсолютна похибка: від {wide_error_limits_a[0][0]} до {wide_error_limits_a[0][1]}")
print(
    f"   Відносна похибка: від {wide_error_limits_a[1][0]} до {wide_error_limits_a[1][1]}")
print(
    f"б) Граничні абсолютні та відносні похибки у широкому розумінні для числа {value_b}:")
print(
    f"   Абсолютна похибка: від {wide_error_limits_b[0][0]} до {wide_error_limits_b[0][1]}")
print(
    f"   Відносна похибка: від {wide_error_limits_b[1][0]} до {wide_error_limits_b[1][1]}")
