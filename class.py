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

