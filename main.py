class Computer:
    def __init__(self):
        self.max_price = 1000


    def get_max_price(self):
        return self.max_price
    

    def set_max_price(self, price):
        self.max_price = price


comp = Computer()
print(comp.get_max_price())

comp.set_max_price(1200)
print(comp.get_max_price())