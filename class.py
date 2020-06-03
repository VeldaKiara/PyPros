class Facade: #an empty class
  pass
#instantiation of a class
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

#Methods are functions that are defined as part of a class. 
# Convention recommends that we name this first argument self.
#  Methods always have at least this one argument.

class Rules:
      pass
      def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."
    
problem = Rules()
print(problem.washing_brushes())
#addition of more than one param i.e more than self
class DistanceConverter:
      kms_in_a_mile = 1.609
      def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

class Circle:
    pi = 3.14 #def class
  
    def area(self, radius): #def method
        return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)

#dunder methods/constructors
# __init__ method  is used to initialize a newly created object.
#  It is called every time the class is instantiated.
class Circle:
    pi = 3.14
  
  # constructor 
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)
print(teaching_table)

#data held by an object is referred to as an instance variable.
#The data held by an object is referred to as an instance variable.
#  Instance variables aren’t shared by all instances of a class
#  — they are variables 
# that are specific to the object they are attached to.

class Store:
    pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#Attribute functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))
    
  
  #addition of a class that uses instance variables in a search engine
  class SearchEngineEntry:
    secure_prefix = "https://"
    def __init__(self, url):
      self.url = url

    def secure(self):
      return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")

print(codecademy.secure())
# prints "https://www.codecademy.com"
wikipedia = SearchEngineEntry("www.wikipedia.org")
print(wikipedia.secure())
# prints "https://www.wikipedia.org"

#getting circumference and radius of a circle
class Circle:
    pi = 3.14
    def __init__(self, diameter):
      print("Creating circle with diameter {d}".format(d=diameter))
       # Add assignment for self.radius here:
    
      self.radius = diameter / 2
    
    def circumference(self):
      return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#We can use the dir() function to investigate an 
# object’s attributes at runtime. dir() is short for
#  directory and offers an organized presentation
#  of object attributes.

class FakeDict:
       pass
fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
#functions are also objects
print(dir(5))
def this_function_is_an_object():
   return "happy"
print(dir(this_function_is_an_object))

#dunder method called __repr__. This is a method we can use to tell 
# Python what we want the string representation of the class to be.
#  __repr__ can only have one parameter, self, and must return a string.

class Circle:
    pi = 3.14
  
    def __init__(self, diameter):
      self.radius = diameter / 2
  
    def area(self):
      return self.pi * self.radius ** 2
  
    def circumference(self):
      return self.pi * 2 * self.radius
  
    def __repr__(self):
      return "Circle with radius {radius}".format(radius=self.radius)
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


class Student: #student class
    def __init__(self, name, year): #constructor/dunder method
      self.name = name  #attributes 
      self.year = year
      self.grades = []
  
    def add_grade(self, grade):
      if type(grade) is Grade:
        self.grades.append(grade)
    def get_average(self, average):
      average = sum(self.grades)/len(self.grades)
      self.average = average   

class Grade:
  minimum_passing = 65
  
  def __init__(self, score): #constructor 
    self.score = score
  def grade(self, grade):
    if grade >= minimum_passing:
      print("You have a passed.")
      self.grades.append(grade)
   
#instance variables    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))