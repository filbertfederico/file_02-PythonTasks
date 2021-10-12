a = eval(input("enter length of edge a:"))
b = eval(input("enter length of edge b:"))
c = eval(input("enter length of edge c:"))

if a+b>=c and b+c>=a and c+a>=b :
    print (a+b+c)
else :
    print ("input is invalid")