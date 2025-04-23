"""
dish = []

def func():
    while len(dish) <= 5:
        value = input("enter a value ")
        dish.append(value)
    print(dish)

func()

"""
"""
cards = []

for x in range(3,80):
    cards.append(x)

print(cards)
"""
'''

nums = [x*2 for x in range(1,20)]
print(nums)'''


boy = ["adam", "ted", "maguire", "toby"]

boys = ['#' + y for y in boy]
print(boys)

caps = [a.capitalize() for a in boy]
print(caps)

nots = [c for c in boy if c[1] != 'adam']
print(nots)