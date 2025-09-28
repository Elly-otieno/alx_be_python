# Indexing - accessing elements in a list 
my_list = [10, 20, 30, 40, 50]
print(my_list[0])

# slicing - subtract sub-lists from a list using start, stoop and step indices
# list[start:stop:step]

print(my_list[1:3:1])

# reverse a list
print(my_list[::-1])

# append - add at the end of list  - append()

my_list.append(60)
print(my_list)

# remove - delete fro a list remove()
# to delete by index use del keyword

my_list.remove(10)
print(my_list)


del my_list[0]
print(my_list)