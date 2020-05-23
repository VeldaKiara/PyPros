#A dictionary is an unordered set of key: value pairs.
#A dictionary begins and ends with curly braces ({ and }).
''' Each item consists of a key (i.e., “oatmeal”) and a value (i.e., 3)
    Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
    It’s considered good practice to insert a space () after each comma,
     but your code will still run without the space.'''
     
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
sensors["pantry"] = 22 #addition to a dictionary
print(sensors)

#translations from English to Sindarin
translations = {
  'mountain': 'orod',
  'bread': 'bass',
  'friend': 'mellon',
  'horse': 'roch',
}

#keys must always be unchangeable, hashable data types, like numbers or strings.
children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}

#We can create an empty dictionary when we plan to fill it later based on some other input
my_empty_dictionary = {}

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

#to add multiple key : value pairs to a dictionary at once, we can use the .update() method.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739}) #adding more elements to dicts
print(user_ids)

#overwriting elemants
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
#oscar_winners.update({
  #"supporting Actress" : "Viola Davis",
#}) updates only iused in multiple values
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
print(oscar_winners)

#list comprehensions
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine) 
#creating a dict and using list comprehensions
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

#music streaming
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {
  key:value for key, value in zip(songs, playcounts)
}
plays["Purple Haze"] = 1

plays.update({
  "Respect" : 94
})
print(plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)

#getting a key in a dict
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"], 
    "fire": ["Aries", "Leo", "Sagittarius"], 
    "earth": ["Taurus", "Virgo", "Capricorn"], 
    "air":["Gemini", "Libra", "Aquarius"]
    }
print(zodiac_elements["earth"])
print(zodiac_elements["fire"]) #getting values from keys in dict

#avoiding key errors
zodiac_elements['energy'] = "Not a Zodiac element"
print(zodiac_elements["energy"])

#Try/Except to Get a Key
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30
key_to_check = "matcha"
try:
  print(caffeine_level[key_to_check])
except KeyError:
  print("unknown Caffeine level")

#using .get() method
user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
    }
tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

print(tc_id)
print(stack_id)

#deleting  a key .pop()
available_items = {
    "health potion": 10, 
    "cake of the cure": 5, 
    "green elixir": 20, 
    "strength sandwich": 25, 
    "stamina grains": 15, 
    "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

#.keys() method that returns a dict_keys object.
#dict_keys object is a view object, which provides a
#  look at the current state of the dicitonary,
#  without the user being able to modify anything.

user_ids = {
    "teraCoder": 100019, 
    "pythonGuy": 182921, 
    "samTheJavaMaam": 123112, 
    "lyleLoop": 102931, 
    "keysmithKeith": 129384
    }
num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
    }

users = user_ids.keys() #gets keys form userid
lessons = num_exercises.keys() #gets keys from num_exercises

print(users)
print(lessons)

#.values() method that returns a dict_values object just like .keys() for key values
num_exercises = {
    "functions": 10, 
    "syntax": 13, 
    "control flow": 15, 
    "loops": 22, 
    "lists": 19, 
    "classes": 18, 
    "dictionaries": 18
    }
total_exercises = 0
#iterating through it and adding exercise to total exercise
for exercise in num_exercises.values():
  total_exercises += exercise
  print(total_exercises)
  
#to get both the keys and the values use the .items() method.
pct_women_in_occupation = {
    "CEO": 28, 
    "Engineering Manager": 9, 
    "Pharmacist": 58, 
    "Physician": 40, 
    "Lawyer": 37, 
    "Aerospace Engineer": 9
    }
for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
  
  #tarot cards
  tarot = { 
           1: "The Magician", 
           2: "The High Priestess", 
           3: "The Empress", 
           4: "The Emperor", 
           5: "The Hierophant", 
           6: "The Lovers",
           7: "The Chariot", 
           8: "Strength",
           9: "The Hermit", 
          10: "Wheel of Fortune", 
          11: "Justice", 
          12: "The Hanged Man", 
          13: "Death", 
          14: "Temperance", 
          15: "The Devil", 
          16: "The Tower", 
          17: "The Star", 
          18: "The Moon", 
          19: "The Sun", 
          20: "Judgement",
          21: "The World",
          22: "The Fool"
        }
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for time, card in spread.items():
  print("Your " + str(time)+ " is the " + str(card)+ " card. " ) 