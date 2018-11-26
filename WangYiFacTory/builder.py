class Burger():
    name = ""
    price = 0.0
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price = price
    def getName(self):
        return self.name
class cheeseBrger(Burger):
     def __init__(self):
         self.name = "cheese burger"
         self.price = 10.0
class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = 'spicy chicken burger"'
        self.price = 15.0

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price = price
    def getName(self):
        return self.name
class chips(Snack):
    def __init__(self):
        self.name = 'chips'
        self.price = 6.0
class chickenWings(Snack):
    def __init__(self):
        self.name = 'chicken wings'
        self.price = 12.0

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"
    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price
    def getName(self):
        return self.name

class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0

class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

class order():
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def __str__(self):
        print('==================================')
        info = ("Burger:%s" % self.burger.getPrice())
        return info

    def show(self):
        print("Burger:%s" % self.burger.getName())
        print("Burger:%s" % self.burger.getPrice())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())

class orderBuilder():
     bBurger = ""
     bSnack = ""
     bBeverage=""
     def addBurger(self,xBurger):
         self.bBurger = xBurger
     def addSnack(self,xSnack):
         self.bSnack = xSnack
     def addBeverage(self,xBeverage):
         self.bBeverage = xBeverage
     def build(self):
        return order(self)

class orderDirector():
    order_builder = ""
    def __init__(self,order_builder):
        self.order_builder = order_builder
    def createOrder(self,burger,snack,beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()
if  __name__=="__main__":
    order_builder=orderBuilder()
    order_director = orderDirector(order_builder)
    order_1=order_director.createOrder(cheeseBrger(),chips(),coke())
    order_1.show()
    print(order_1)






