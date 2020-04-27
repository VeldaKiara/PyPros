def greet_customer(special_item):
    print("Welcome to Engrossing Grocers.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
"""
 The definition heading for 
greet_customer(), the special_item is referred to as a formal parameter. 
This variable name is a placeholder for the 
name of the item that is the grocery’s special today.
"""
def mult_two_add_three(number):
    
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
mult_two_add_three(5)

#the first line defines a function
#the function is called and passes the number inside the call
def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
def mult_x_add_y(number, x, y):
     print(number*x + y)
  
mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)
""" 
positional arguments are assignments that 
depend on their
positions in the function call
We can also pass these arguments as 
keyword arguments, where we explicitly 
refer to what each argument 
is assigned to in the function call.
We can use keyword arguments to 
make it explicit what each of our arguments
 to a function should refer 
to in the body of the function itself.
We can also define default arguments 
for a function using syntax very similar
 to our keyword-argument syntax,
  but used during the function definition. 
  If the function is called without
   an argument for that parameter, 
it relies on the default.
"""

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print(" I am " + str(my_age) + " years old and my dad is "+ str(dads_age))

#Returning multiple values
def get_boundaries(target, margin):
      low_limit = target - margin
      high_limit = target + margin
      return low_limit, high_limit

low, high = get_boundaries(100, 20)
print("Low limit: "+str(low)+", high limit: "+str(high))

#global definition of variables
current_year = 2048
def calculate_age(birth_year):
  age = current_year - birth_year
  return age
print(calculate_age(1970))

#functions 
def repeat_stuff(stuff, num_repeats = 10):
      return stuff * num_repeats
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
song = repeat_stuff(lyrics)
print (song)