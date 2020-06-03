#inheritance 
#child class inherits from super or base class
class Bin:
    pass

class RecyclingBin(Bin):
  pass
"""An Exception is a class that inherits from Python’s Exception class.
issubclass() is a Python built-in function that takes two parameters.
issubclass() returns True if the first argument is a subclass of the
second argument. It returns False if the first class is not a 
subclass of the second. issubclass() raises a TypeError if 
either argument passed in is not a class."""

issubclass(ZeroDivisionError, Exception)
# Returns True because it is a subclass of Exception.

#out of stock exception
class OutOfStock(Exception): 
      pass
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
candle_shop.buy('green')

#overriding methods
#An overridden method is one that has a different definition from its parent class
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
      
class Admin(User): #overiding of admin to edit message
  def edit_message(self, message, new_text):
    message.text = new_text