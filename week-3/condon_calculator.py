
# Defines addition function
def add(x, y):
    return x + y

# Defines subtraction function
def subtract(x, y):
    return x - y

# Defines division function
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Defines multiplication function
def multiply(x, y):
    return x * y

# Variables to test
num1 =  8
num2 =  2

# Calls functions passing the variables to create strings
add_result = str(num1) + " + " + str(num2) + " is " + str(add(num1, num2))
subtract_result = str(num1) + " - " + str(num2) + " is " + str(subtract(num1, num2))
divide_result = str(num1) + " / " + str(num2) + " is " + str(divide(num1, num2))
multiply_result = str(num1) + " * " str(num2) + " is " str(multiply(num1, num2))

# Prints
print(add_result)
print(subtract_result)
print(multiply_result)
print(divide_result)


