# Q1: Create a variable called city and store the name of your city in it. Print the value of the variable.
#  Then print the type of the variable.
# Solution:

# city = "Bannu"
# print(city)

# Q2: Store your name in a variable, your age in another variable, and your height in a third variable.
#  Print them all in one line using f-string.

# Solution
# name = "awais khan"
# age = 23
# height = 5.6
# print(f"Name: {name} Age: {age} Height: {height}")

# Q3: Ask the user to enter two numbers. Store them in variables, add them,
#  and print the result. Make sure the result is shown as a number (not as string concatenation).

# Solution

# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# result = num1+num2

# print(f"Num1 and Num2 have sum is : {result}")

# Q4: Store the value True in a variable is_student. Print the variable and also print its type.
#  Then change the variable to False and print it again.
# Solution
# is_student = True
# is_student = False

# print(type(is_student))


# # Q5
# Create three variables:
# x = integer
# y = float
# z = string containing a number (example: "25")

# Now:
# Convert z into an integer and add it to x.
# Add x and y.
# Print the results and their types.

# Solution:

# x = 23
# y = 232.2
# z = "34"

# z = int(34)
# x = x+z
# add = x+y

# print(add)


# Q6: Write a program that asks the user for their name and age.
# Store them in variables.

# Print: "Hello <name>, in 5 years you will be <age+5>".
# (Hint: Remember input() always returns a string.)
# name = input("Enter the name: ")
# age = int(input('Enter the age '))

# print(f"Hello {name}, in 5 years you will be {age+5} ")


# Q7: Create a variable price with a float value (e.g., 199.99).

# Convert it to an integer and print it.
# Convert it to a string and print it.
# Finally, check the type after each conversion.

# Solution:
price = 120.2

price_int = int(price)
price_str = str(price)

print(f"Price in integer:{type(price_int)}")
print(f'Price in str: {type(price_str)}')


