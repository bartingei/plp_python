import math
import random
import datetime
import matplotlib

num1 = 22
num2 = 2
num3 = 100
print(math.pow(num1,num2))

print("square root is: ",math.sqrt(num3))

names = ["solo", "neema", "jp", "ivy", "king", "samantha"] 
print(random.choice(names))

print(random.randint(1,10))

today = datetime.date.today()
print("today's date is: ",today)

now = datetime.datetime.now()
print(now)
