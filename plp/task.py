"""Tasks:

Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.



These tasks should test your understanding of basic concepts related to lists, tuples, dictionaries, and sets in Python. Good luck!"""



#list
nums = []
ranges = int(input("list length is? "))
for i in range(ranges):
    new = input("Enter a number: ")
    nums.append(new)
print(nums)

sum = 0
for j in nums:
    sum += int(j)
print("sum: ",sum)

#tuple
books = ("To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "The Catcher in the Rye"
)
for book in books:
    print("\n", book,"\n\n")


#dictionary
person = {}
person["name"] = input("Name: ")
person["age"] = input("age: ")
person["colour"] = input("favorite colour: ")

print(person)

#sets
set1 = set()
vals = int(input("how many values for the set1: "))
for x in range(vals):
    x = input("Enter an integer")
    set1.add(x)
print(set1)

set2 = set()
val = int(input("how many values for the set2: "))
for y in range(val):
    y = input("Enter an integer")
    set2.add(y)
print(set2)

set3 = set1.intersection(set2)
print(set3)


words = []
list_len = int(input("What is the length of the list? "))
for word in range(list_len):
    word = input("Enter a word:  ")
    words.append(word)

print(words)

for z in words:
    if(len(z) % 2 == 1):
        print(z)
    else:
        continue