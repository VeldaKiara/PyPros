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
