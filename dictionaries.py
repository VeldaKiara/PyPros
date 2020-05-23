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