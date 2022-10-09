import math as m
a=float(input("Введіть нижню границю"))
b=float(input("Введіть верхню границю"))
h=float(input("Введіть значення кроку"))

for bar in range (100):
    func = 3-m.log1p(abs(bar-6))+m.cos(bar)
    
    print(func)