import math
x=int(input("введіть x"))
if x>=3:
    y=math.sin(x)
    print(y)
elif 0<=x<3:
    y=math.cos(x)
    print(y)
else:
    y=math.tan(x)
    print(y)
