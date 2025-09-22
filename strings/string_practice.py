
# 🔹 Q1 (Reverse with step)
# Given a string s = "programming",
# Print the string reversed using slicing.

# Solution:
# s = "Programming"
# s = s[::-1]
# print(s)

# 🔹 Q2 (Middle character(s))
# Ask the user to enter a string.
# If the string length is odd, print the exact middle character.
# If the string length is even, print the two middle characters.

# Solution

# str = input("Enter the string:")
# length = len(str)

# if length%2 == 1:
#     mid = length//2
#     print(f"Middle value of the string:{str[mid]}")
# else:
#     mid1 = length//2-1
#     mid2 = length//2
#     print(f"Middle character:{str[mid1]}{str[mid2]}")


# 🔹 Q3 (Substring extraction)

# Given text = "Python is powerful",
# Extract the substring "thon" using slicing.
# Extract the substring "power" without directly writing the indexes (hint: use negative indexing).

# text = "Python is powerful"

# print(text[2:6])
# print(text[9:])

# 🔹 Q4 (Custom reverse slice)

# Ask the user to enter a word.
# Print the word but without the first and last characters.
# Then reverse that new string using slicing.

# user = input("Enter the word:")

# text = user[1:-1]
# print(text)


# 🔹 Q5 (Challenge – Palindrome check with slicing)

# Write a program that asks the user to enter a word.
# Check if the word reads the same forwards and backwards (palindrome).
# Print True if it is, otherwise False.
# (Hint: use slicing [::-1])
# user = input("Enter the word:")



