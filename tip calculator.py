x = int(input("enter subtotal :"))
y = int(input("enter tip amount :"))

print ("subtotal : $",'%0.2F'%x)

z =x*(y/100)
print ("tip :","$",'%0.2F'%z)

final = x+z
# print("total :","$",'%3.2F'%final)
print("total : $","{:3,.2F}".format(final))
