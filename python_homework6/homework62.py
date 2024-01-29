#Write a program that takes a string as input and counts the
# number of vowels (a, e, i, o, u) in the string. Use a for
# loop, an if statement, and the in operator to check if a
# character is a vowel.

string = input("Enter a string: ")
vowels = 0
for i in string:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        vowels += 1
print("No of vowels are:", vowels )