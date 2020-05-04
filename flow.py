my_baby_bool="true" 
print(type(my_baby_bool)) #prints string because it is not boolean
my_baby_bool_two = True
print(type(my_baby_bool_two)) #prints bool because of capitalized T
#boolean features
#if else statements
def dave_check(user_name):
      if user_name == "Dave":
        return "Get off my computer Dave!"
      if user_name == "angela_catlady_87":
        return "I know it is you Dave! Go away!"
  
# Enter a user name here, make sure to make it a string
user_name = "Dave" 

print(dave_check(user_name))

 #if else statements 
def greater_than(x, y):
      if x > y:
        return x
      if y > x:
        return y
      if x == y:
        return "These numbers are the same"
    
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
  
print(graduation_reqs(120))