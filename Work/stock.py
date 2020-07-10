# stock.py
# Exercise 4.1: Objects as Data Structures
# https://github.com/wlpygit/practical-python/blob/master/Notes/04_Classes_objects/01_Class.md#exercise-41-objects-as-data-structures

# Exercise 4.2: Adding some Methods

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def __repr__(self):
        return f'Stock({str(self.name)},{str(self.shares)},{str(self.price)})'

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        self.shares -=n
        return

