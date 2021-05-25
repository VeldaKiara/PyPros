# Write your in_range function here:
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
#first number is the starting point, middle number is 
# the ending point and the third is the range between numbers
list1 = range(5, 15, 3) 
list2 = range(0, 40, 5)