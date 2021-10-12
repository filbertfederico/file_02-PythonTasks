ta = int(input("enter temperature in Fahrenheit :"))
v = int(input("enter wind speed miles per hour :"))

while ta < -58 or ta > 41 :
    print ("Temperature must be between -58F and 41F")
    ta = int(input("please re-enter the temperature between -58F and 41F :"))
while v < 2 :
    print ("Speed must be greater than or equal to 2")
    v = int(input("Please re-enter the wind speed miles per hour :")) 
else :
    twc = 35.74 + 0.6215*ta - 35.75*(v**0.16) + 0.4275*ta*(v**16)

print ("%2.3f"%twc)

# still in progress
