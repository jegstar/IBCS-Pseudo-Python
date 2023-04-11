from ib_array import Array
from ib_collection import Collection

# create an empty array of strings
string_arr = Array(5, 'string')
print(string_arr)

# change item in array
string_arr[2] = "New value"
print(string_arr)

# loop through array
for item in string_arr:
    print(item)



# Collections
col = Collection()

print(col.isEmpty())

col.addItem("a")
col.addItem("b")
col.addItem("c")

print(col)
while col.hasNext():
    print(col.getNext())


######### Collections problems ###############
# Write a method that inputs a persons expenses as a float and expense class as a string.
# EG 
# 2.65, travel
# 4.99, food
# The user has the following classes available: food, travel, housing, clothing, other
# Add each to a collection for its correct type.
# Then write an algorithm to calculate the number and total value of each type.
