# OOP
# 1. Inheritance
# 2. Encapsulation # hiding and protecting data
# 3. Abstraction
# 4. Polymorphism


class Item:
    some_var = 1 # class variable - all instances of class can read this
                # self var to refer to an instance of a class
    def __init__(self, name: str, price: float, quantity=0):
        # assert allows validate arguments that we receive
        assert isinstance(name, str), f'name must be a string'
        assert price >= 0, f'Price {price} is not greater than or equal to zero!'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero!'
    
    # maps input paramenters to data attributes (self.name etc)
        self.name = name
        self.price = price
        self.quantity = quantity
    
# Getters and setters are used outside of class to access data attributes 

#@staticmethod


#@classmethod # relate to static method as to regular func that receives 
# Access attribute via getter method - better bc it supports information hiding (bc implementation behing the scenes might change)
# instance of the class
    @property
    def price(self):              # getter
        return self._price

    @price.setter
    def price(self, value):       # setter
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value
    def __repr__(self):
        return f"Item(name={self.name!r}, price={self.price})"

    # destructor only takes self as paramenter
    def __del__(self):
        print(f"Destroying Item: {self.name}, price = {self.price}")
item = Item('Pnone', 1, 9)
print(item)
