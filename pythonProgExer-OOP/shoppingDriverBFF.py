from shoppingListBFF import groceryBFF #import class

def cartBFF(): 
    cart = []
    items = int(input("Items you will order today: "))
    while items < 1 :
        print("Number of items must be at least 1")
        items = int(input("Items you will order today: "))
    for i in range(items):
        print(f"item #{i+1}-")
        name = str(input("Enter food: "))
        weight = float(input("Enter amount of pounds: "))
        while weight < 1 :
            print("Amount of pounds must be greater than 0")
            weight = float(input("Enter amount of pounds: "))
        item = groceryBFF(name,weight)
        cart.append(item) #accumulate items in the list 
    return cart
    
def receiptBFF(cart): #display content of list
    print("Here's a summary of the items purchased:")
    print("-----------------------------")
    for i in cart:
            print(f"Item: {cart[i].getnameBFF()}")
            print(f"Amount ordered: {cart[i].getamountBFF} pounds")
            print(f"Price per pound: ${cart[i].getpriceBFF():.2f}")
            print(f"Price of order: ${cart[i].finalPriceBFF():.2f}")
            print("")
    
def finalPriceBFF(cart):
    total = 0
    for i in range(len(cart)):
        total += cart[i].finalPriceBFF()
    return total
    
def output():
    x= cartBFF()
    receiptBFF(x)
    print(f"Total cost: ${finalPriceBFF(x):.2f}")

output()