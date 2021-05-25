# Write your always_false function here:
def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False