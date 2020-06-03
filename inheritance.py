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
    
#super() gives us a proxy object. 
# With this proxy object, we can invoke the 
# method of an object’s parent class (also called its superclass).
# We call the required function as a method on super():

class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions
        
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions): #creating  a constructor that takes in the same args
    super().__init__(potatoes, celery, onions) #invokes parents class method
    self.raisins = 40

#interfaces
#When two classes have the same method names and attributes, 
# we say they implement the same interface.
#  An interface in Python usually refers to 
# the names of the methods and the arguments they take.

class InsurancePolicy: #superclass
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy): #subclass
  def get_rate(self): #method to get rate
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy): #subclass
  def get_rate(self): #method to get rate
    return self.price_of_insured_item * .00005

#polymorphism used to describe the same syntax 
# doing different actions depending on the type of data.

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

len(a_list)
len(a_dict)
len(a_string)

class Atom:
    def __init__(self, label):
        self.label = label
    
    def __add__(self, other): #adds both molecules and atoms
        return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
