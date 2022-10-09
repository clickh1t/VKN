import math as m
a=float(input("Введіть нижню границю"))
b=float(input("Введіть верхню границю"))
h=float(input("Введіть значення кроку"))

spisok=[]
while a<=b:
    pudge = spisok.append(3-m.log1p(abs(a-6))+m.cos(a))
    a+=h
print(spisok)
