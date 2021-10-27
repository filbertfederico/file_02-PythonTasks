def calc_weight_on_planet(weight=120, gravity =23.1) :
    mass = weight / 9.8
    print(mass * gravity)

print("calc_weight_on_planet(120, 9.8)")
x = calc_weight_on_planet(weight=120, gravity=9.8)
print(x)

print("calc_weight_on_planet(120)")
y = calc_weight_on_planet(weight=120,gravity=23.1)
print(y)

print("calc_weight_on_planet(120, 23.1)")
z = calc_weight_on_planet(weight=120,gravity=23.1)
print(z)