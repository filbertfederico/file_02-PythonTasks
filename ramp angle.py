import math

m = int(input("input mass of the cart:"))
F = float(input("input force to push the cart :"))
g = 9.8
a = math.sinh(F/(m*g))
degree = math.degrees(a)
print('%.1F'%degree,"degrees")


