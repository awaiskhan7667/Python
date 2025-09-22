# Q1: Create two variables x = 10 and y = 20.
# Print whether x is greater than y, equal to y, or less than y using comparison operators.

# Solution:

# x = 20
# y = 30

# print(f"x is greater than y: {x>y}")
# print(f"x is less than y: {x<y}")
# print(f"x is equal to y: {x==y}")

# Q2: Ask the user to enter their age.
# Print:
# True if the age is between 18 and 30 (inclusive).
# False otherwise.
# (Hint: use and operator).

# Solution:

# age = int(input("Enter the age:"))

# print(age>=18 and age<=30)

# Q3: Start with num = 10.
# Use assignment operators step by step to:

# Add 5 to it.
# Multiply it by 2.
# Subtract 4 from it.
# Divide it by 3.
# Print the result after each operation.

# Solution:

# num = 10
# num +=5
# num -=4
# num *2
# num /=3
# print(f"Num: {num}")


# Q4: Write a small program that asks the user for two integers.
# Then:
# Check if the first number is divisible by the second (use %).
# Print True if it is divisible, else False.
# Also print whether the first number is greater than 50 AND even (use % and and).

# Solution:

# num1= int(input("num1: "))
# num2= int(input("num2: "))

# if num1 % num2:
#     print(True)
# else:
#     print(False)

# print(num1 > 50 and num1%2==0)

# Q6: Write a program that asks the user to enter three integers: a, b, and c.

# Do the following step by step:
# Check if a is the largest of the three numbers (use comparison operators).
# Check if all three numbers are positive (use logical operator and).
# Create a variable sum_val = a + b + c.
# If sum_val is even, divide it by 2 (use arithmetic + assignment operator).
# If it is odd, multiply it by 3.
# Finally, print:
# The values of a, b, c.
# Whether a was the largest.
# Whether all numbers were positive.
# The final value of sum_val.

a =int(input("Enter the value of a:"))
b =int(input("Enter the value of b:"))
c =int(input("Enter the value of c:"))

if a>b and a>c:
    print("a is the largest value")
elif a and b and c >= 0:
    print("All the values are positives")

sum_val = a+b+c
print(sum_val)

if sum_val % 2 == 0:
    print("sum_value is even")
    sum_val/=2
    print("Divided by 2")
else:
    sum_val *=3
    print("Multiply by 3")