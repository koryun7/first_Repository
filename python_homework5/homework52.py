#Write a Python program to get the largest number from a list.
numbers = [5, 7, 3, 9, 11]
max = numbers[0]
for a in numbers:
    if a > max:
        max = a
print("Max:", max)

