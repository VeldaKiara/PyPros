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