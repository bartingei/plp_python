"""
Instructions:

Basic Calculator Program

Create a simple Python program that asks the user 
to input two numbers and a mathematical operation
 (addition, subtraction, multiplication, or division).
Perform the operation based on the user's input and print the result.
Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

"""

num1 = input("Enter the first number  ")
num2 = input("Enter the second number  ")
operation = input("Operation type?  + , - , * ")

if(operation == '+'):
    sum = int(num1) + int(num2)
    print("sum of ",num1, " and ", num2 ,"is: ", sum)
elif(operation == "-"):
    difference = int(num1) - int(num2)
    print("difference of ",num1, " and ", num2 ,"is: ", difference)
else:
    product = int(num1) * int(num2)
    print("product of ",num1, " and ", num2 ,"is: ", product)
