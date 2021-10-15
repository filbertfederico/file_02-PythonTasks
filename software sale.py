x = int(input("enter amount of packages purchased :"))

if x<10 :
    print("discount amount @ 0% : $ 0.00")
    a = x*99
    print("total amount : $",'%.2f'%a)
else :
    if x >= 10 and x<= 19 :
        y = 10
    if x >= 20 and x<= 49 :
        y = 20
    if x >= 50 and x<= 99 :
        y = 30
    if x >= 100 :
        y = 40

    disc = (99*x*(y/100))
    total = (99*x)-(99*x*(y/100))
    print("discount amount @ {}% : $ {:.2f}".format(y,disc))
    print("total amount : $ {:,.2f}".format(total))
