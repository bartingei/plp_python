"""
#creating a function
def greet():
    print("greetings from the greet function")
    print("goodbye from the greet function")

def wake():
    print("wake up you dumb fuck! ")
    print("stay hard") 

#function taking an argument
def personal(name):
    print("Hello "+ name)
#calling the function
greet()

wake()

personal("johnpaul")
"""
"""
def size(length, width):
    area = length * width
    perimeter = 2 * int(length + width)
    price = 1000 * int(area)
    return area, perimeter, price

#print("area is: ", area )

print("length, width, price ", size(10,7))
"""


"""
def delivery(address):
    if address == True:
        print("Enter your adress")
    else:
        print("goodbye")

delivery(True)
"""

prices = [213,453,12,43,123,342]
total = sum(prices)
highest = max(prices)
print(total)
print(highest)
print(sorted(prices))

#sorting in descending order
print(sorted(prices, reverse = True))