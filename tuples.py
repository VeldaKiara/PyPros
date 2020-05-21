#tuples are immutable, they cannot be changed.
#tuples use ()
#unpacking a tuple uses the number of info
#an example of unpacking
#my_deets = (Velda, 22, web dev)
#how to unpack:
#name,age, occupation = my_deets
#name
#prints Velda
#tuples can also have trailing commas.
#the order of tuples is important.

dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print(breed)
# A for loop lets us perform an 
# action on each item in a list. 
# Using each element of a list is known as iterating.

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for sport in sport_games:
  print(sport)
  
promise = "I will not chew gum in class" 
for i in range(5): #using range to print promise 5 times
  print(promise)
  
#A loop that never terminates is called an infinite loop.
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for students in students_period_A: #goes through a and appends to b
  students_period_B.append(students)
  print(students)
  
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break
  #continue keyword
  
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
  
 for age in ages:
      if age < 21:
    continue
  print(age)
  
#while loop
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []
while len(students_in_poetry) < 6:
  students_in_poetry.append(all_students.pop()) #everytime a student is popped s/he is appended
  print(students_in_poetry)
  
#nested loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
for location in sales_data:
      print(location)
      for scoops in location:
        scoops_sold += scoops
        print(scoops_sold)

#list compressions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]   
can_ride_coaster = [ height for height in heights if height > 161]
#the first heightis added to the second height, heights the name of list and addition of the if statement
print(can_ride_coaster)
    
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp*(9/5) + 32 for temp in celsius] #converting temp to fahrenheit from celsius
print(fahrenheit)


single_digits=[0,1,2,3,4,5,6,7,8,9]
squares = []

for single in single_digits:
  print(single)
  
  