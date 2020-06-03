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