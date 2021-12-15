# A function is a MODULE OF CODE that accomplishes a specific
# task. Functions can be CALLED to execute the code inside of them
# Functions essentially take something, do something, and return something

# In Python, we define functions using the def keyword
# Function designed to say hello


def sayHello():
    print('HELLO')


# calling the function multiple times
# function calls are followed by A DOUBLE BRACKET
sayHello()
sayHello()
sayHello()

# functions can take ARGUMENTS/PARAMETERS
# this function TAKES a number as input and stores it in the variable num

# in the funciton definition, a variable inside the
# brackets means the function is EXPECTING that argument to be passed


def printNumber(num):
    print(num)


# calling the function and PASSING 3 AS A PARAMETER
# within the function the 3 will be stored in the num variable
printNumber(3)

# you can also define functions that take MULTIPLE ARGUMENTS
# this one takes three numbers, and stores them in num1, num2, and num3 respectively


def printNumbers(num1, num2, num3):
    print(num1, num2, num3)

# Functions can also RETURN a value which can be used OUTSIDE of the function
# By default, functions return None (nothing). However, you can return any value
# you want

# For example, if you wanted to create a function that RETURNS the sum of two given values,
# you can define this function


def add(num1, num2):
    return num1 + num2

# since this function is RETURNING the sum, you can use it outside of the code like this


# theSum contains 3, as RETURNED by the add function. In other words, add(1, 2) EVALUATES to 3 in this case
theSum = add(1, 2)

# if you try to store the value of a function that doesn't return a value, it will be None (b/c functions return None by default)
# printNumbers returns nothing even though it prints stuff to the terminal, so the value of theNothing is None
theNothing = printNumbers(1, 2, 3)
