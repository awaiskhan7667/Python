# Type conversion
# a = 12
# b = 34.3

# # Here will print float value, because float is superior, how, bcs float has  store more detail than int.
# sum = a + b 
# print(sum)

# String 

# a = "23"
# b = 23.3
# sum = a + b 
# # TypeError: can only concatenate str (not "float") to str: This error says that can not cancatenate string with float only str to str
# print(sum)


# TYPE CASTING

# here you can only change number and not a string means(awais, any str) just an number  and also int can convert to string
# a = int("3")
# b = 23
# sum = a + b

# print(type(a))
# print(sum)


# # Input function always print the string unless you define the int(input) like this.
# num  = input("Enter the value ")
# print(num)
# print(type(num))

# Let's Practice
#  Write a program to input 2 numbers and print their sum ?

num1 = int(input("Enter the num 1: "))
num2 = int(input("Enter the num 2: "))

sum = num1 + num2
print(f"Sum of num1 and num2:{sum}")