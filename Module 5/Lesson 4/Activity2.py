class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Selling price: {self.__maxprice}BDT")

    def updatedprice(self,updated_price):
        self.__maxprice = updated_price


c = Computer( )
c.sell()

c.__maxprice = 1200
c.sell()

c.updatedprice(1200)
c.sell()