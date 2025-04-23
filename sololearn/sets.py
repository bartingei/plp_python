#defined using curly brackets
#can have data types of diff values
#are mutable however append() will not work since it works with ordered collection
#are unordered
#do not support indexing and slicing
#can not have duplicates like lists and tuples, duplicates are ignored
movies = {"the notebook","you", "Adam's project", "you", "tron"}
print(movies)

#adding a value
movies.add(2321)
print(movies)

#removing a value
movies.remove("Adam's project")
print(movies)

#clear() is used to remove all the items
movies.clear()
print(movies)

#union() is used to combine two or more sets
set1 = {" :marks: "}
set2 = {9999}
set3 = set1.union(set2)
print(set3)

#difference is used to return common values in the set
fruits1 = {"mangoes", "apple", "orange", "pineapple"}
fruits2 = {"Orange", "peach", "grapes"}
unique = fruits1.difference(fruits2)
print(unique)