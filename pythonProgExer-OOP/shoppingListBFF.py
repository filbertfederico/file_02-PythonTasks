class groceryBFF: #initialize
    def __init__(self,food,amount):
        self.__food = food
        self.__amount = amount
        self.__price = self.priceBFF()
        self.finalPrice = self.finalPriceBFF()
    
    def getnameBFF(self): #food name
        return self.__food
    def getamountBFF(self): #quantity
        return self.__amount
    
    def __pricelist(self): #price list for foods
        if self.__food == "Dry Cured Iberian Ham":
            self.__price = 177.80
        elif self.__food == "Wagyu Steaks":
            self.__price = 450.00
        elif self.__food == "Matsutake Mushrooms":
            self.__price = 272.00
        elif self.__food == "Kopi Luwak Coffee":
            self.__price = 306.50
        elif self.__food == "Moose Cheese":
            self.__price = 487.20
        elif self.__food == "White Truffles":
            self.__price = 3600.00
        elif self.__food == "Blue Fin Tuna":
            self.__price = 3603.00
        elif self.__food == "Le Bonnotte Potatoes":
            self.__price = 270.81
    
    def priceBFF(self): #get price
        self.__pricelist()
        return self.__price
    
    def finalPriceBFF(self): #price cost
        self.finalPrice = self.__price * self.__amount
        return self.finalPrice 


