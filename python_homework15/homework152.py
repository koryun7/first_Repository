# Random Password Generator:
# Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers, and symbols).
# Ogtvel random u string module-neric (string.ascii_letters,
# string.digits,string.punctuation, )
import random
import string

length = int(input("Enter length: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(length):
    choice = random.choice(chars)
    password += choice

print(password)
