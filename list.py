#adding first names
first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
#adding an empty list
age = []
#adding of age
age.append(42)
#adding age
all_ages = age + [32, 41, 29]
#adding zip
name_and_age = zip(first_names, all_ages)
#adding range
ids = range(4)

#2 is the starting point, 20 is the last number and the last 2 is the difference between the numbers expected
list1 = range(2, 20, 3)
list1_len = len(list1) #len is for the length of the list
print(list1_len)

employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 =(employees[4]) #Index to call item number.
print(len(employees)) #length of lists.

print(employees[8]) #traceback because out of range i.e indexxerror
print(employees[6]) 

#use the index -1 to select the last item of a list, 
# even when we don’t know how many elements are in a list.

shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element =shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)

#to use slicing 
#letters[start:end], syntax
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:2]
print(beginning)
beginning = suitcase[0:4] #prints shirts to pants, first 4 elemnts
print(beginning)
middle =suitcase[2:4] #prints the middle elements
print(middle)

fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits[0:3])#first three elements
#output['apple', 'banana', 'cherry']

print(fruits[:3]) #also prints first 3 elements
#output['apple', 'banana', 'cherry']

print(fruits[2:]) #last  two items on the list
#output['cherry' , 'date']

print(fruits[-3:]) #counts from backwards
#output['banana', 'cherry', 'date']

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3] #first three elements
end = suitcase[4:] #last elements

#how to count the number of words or letters using count
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()

names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
# sort(names)


cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()

