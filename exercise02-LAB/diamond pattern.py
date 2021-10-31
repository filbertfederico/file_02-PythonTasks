h = int(input("input the height of the diamond:"))
# h = 5
for i in range(h) :
    print(" " * (h-i), end="")
    for j in range(1,i+2) :
        print("*", end="")
    for k in range(i,0,-1):
        print("*", end="")
    print()
    
a = h-3
for i in range(1,h) :
    print(" " * (i+1), end="")
    for j in range(h-i,0,-1):  
        print("*", end="")
    for k in range(a,-1,-1):  
        print("*", end="")
    a=a-1
    print()    
