#lists are represented by []
#lists can hold data types of different types
'''
ages = [12, 34, 53, 14] 
print(ages)

objects = ["JP", 2123, "brad", True, False, 2.32 ]
print(objects)
print(objects[3])
'''
vehicle = 'airplane'
   
#list unpacking, this also works with tuples
details = [6, "April", 2005]
day, month, year = details
print(day)
print(month)
print(year)

#using rest is used to unpack all other members of the list or tuples 
#used when the list or tuple has many items
obj = ["JP", 2123, "brad", True, False, 2.32 ]
name1, *rest = obj
print(name1)
print(rest)