import math
x=float(input("Введіть x"))
def f(x1):
    return 3*math.tan(x)/math.log1p(math.cos(x)+4)+abs(x-pow(x,2))

print(f(x))