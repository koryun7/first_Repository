#Write a Python program to get the smallest number from a list.
numbers = [5, 7, 3, 9, 11]
min = numbers[0]
for a in numbers:
    if a < min:
        min = a
print("Min:", min)