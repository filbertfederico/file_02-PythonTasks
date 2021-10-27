def num_atoms(mass,weight=196.97):
    avo = 6.022*(10**23)
    print (mass/weight*avo)

print("num_atoms(10)")
x = num_atoms(10)
print(x)

def num_atoms(mass,weight):
    avo = 6.022*(10**23)
    print (mass/weight*avo)

print("num_atoms(10, 12.001)")
num_atoms(10, 12.001)

def num_atoms(mass,weight):
    avo = 6.022*(10**23)
    print (mass/weight*avo)

print("num_atoms(10, 12.001)")
num_atoms(10, 1.008)


# weight is 10 grams
# element amount for gold is 79
#atomic number for gold is 196.97