# Fill in the contents of the is_old_enough_to_drive function. This function takes in a number, called age, and returns whether a person of this age old enough to legally drive in the United States. If the person is old enough to drive, the function should return True. If they are not old enough to drive in the united states, the function should return False. Notes:

#     The legal driving age in the United States is 16

# output = is_old_enough_to_drive(15)
# print(output) # --> False 

def is_old_enough_to_drive(age):
  if age>=16:
    return True
  else:
    return False

print(is_old_enough_to_drive(15))
