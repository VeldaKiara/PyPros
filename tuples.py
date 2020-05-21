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
  
