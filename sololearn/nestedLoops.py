"""
firstName = ["john", "mark", "bruce","jackie"]
lastName = ["paul", "Kaai", "Lee", "chan"]
for i in firstName:
    for j in lastName:
        print(i, j)
"""

"""
items = ["ball", "pen"]
colors = ["Red", "green"]

for i in items:
    for j in colors:
        print(i, j)

for i in range(1,5):
    for j in range(1,4):
        print(i,j)

for k in items:
    for l in range(2):
        print(items)

scores = [21,43,64,76,56,87,98,78,76,89,76,34,54, 65, 43,77,55,88]
for score in scores:
    if score >= 50:
        print(str(score)+" passed")
    else:
        print(str(score)+" failed")
   
prices = [7723,4342,7673,7642,233,454,333,656,754,2342,1333,3421]
total = 0
for price in prices:
    if price <= 1000:
        print("our lowest prices: " + str(price))

for c in prices:
    total += c
    print("total : " + str(total))


countries = ["USA", "France", "Norway", "Spain", "USA", "France", "USA", "Canada"]
count = 0
for a in countries:
    if a == "USA":
        count += 1
        print("USA count is :" + str(count))

for b in countries:
    if 'r' in b:
        print(b)

points = [8.5, 7.9, 6.8, 8.2, 9, 6.3, 8.4]
count = 0
for point in points:
    if point >= 8.0:
        print(str(point)+ "passed")
        count += point
        print(count)

while True:
    text = input("start or stop  ")
    print(text)
    if text == "start":
        print("Game has started: ")
    elif text == "stop":
        print("Game stopped!")
        break

animals = ["dog", "cat", "cow", "goose", "sheep"]
for animal in animals:
    if animal[0] == "l":
        continue
    print(animal)
"""

hour = 1
while hour <= 10:
    if hour == 5:
        hour += 1
        continue
    print("making coffee")
    hour += 1