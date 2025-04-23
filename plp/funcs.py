def introduction(name, age):
    return f'Welcome, {name}, age: {age}'

print(introduction(age = 21, name = "johnpaul"))

#anonymous functions
add = lambda x,y: x + y
print(add(10,11))

subtract = lambda a,b: a - b
print(subtract(100,25))

#factorial
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(0))