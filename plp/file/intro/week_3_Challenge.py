"""
1. Large Power

Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

Define the function to accept two input parameters called base and exponent
Calculate the result of base to the power of exponent
Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False
"""
def power(base, exponent):
    result = base ** exponent
    if result >= 5000:
        return True
    else:
        return False

print(power(3,2))
print(power(9,5))


"""
2.Divisible By Ten

Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False
"""
def divisibility(num):
    if num % 10 == 0:
        return f'{True}, number is divisible by 10'
    else:
        return f'{False}, number is not divisible by 10'
    
print(divisibility(100))
print(divisibility(11 ))