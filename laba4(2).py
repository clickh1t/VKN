import math
def func1(x1, x2, x3, x4):
    y=(pow(x1,2)+math.log1p(abs(x2))-math.sin(x3)*math.sqrt(abs(x4)))
    return(y)
x=float(input("введіть x"))
a=float(input("введіть a"))
b=float(input("введіть b"))
c=float(input("введіть c"))
y=func1(x,a,b,c)
print(y)