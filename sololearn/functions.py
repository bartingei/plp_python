# functions are reusable blocks of code used to perform specific tasks
#string functions
name = "JoHnpaUl"
print(name)

print(name.upper())

print(name.lower())

print(name.capitalize())

print(name.find("l"))

print("robot".find("o"))

songs = ["indie", "rock", "hip hop", "trap", "afro beats"]
songs.append("bongo")
#append is used to add an item to the end of the list
print(songs)
print(len(songs))
#len is used to return the length of the list

#insert function is used to add an element to the list at a specific position 
artists = ["Jcole", "ye", "drake", "Kendrik"]
print(artists)
artists.insert(0, "Glorilla")
print(artists)

#pop() is used to remove an element at a position indicated by its index
print(artists.pop(4))
print(artists)