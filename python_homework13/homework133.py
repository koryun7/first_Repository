# Write a Python program to check whether a given string is number or
# not using Lambda.
x = input("Enter your text!  ")
digit = lambda x : x.isdigit()
print(digit(x))
