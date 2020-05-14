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
