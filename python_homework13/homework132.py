# Write a Python program to find if a given string starts with a given
# character using Lambda.
x = input("Enter the big word! ")
y = input("Enter the character to check! ")
result = lambda x : x[0] == y
print(result(x))

