#Write a Python program to find the second smallest number in a list.
list_1 = [0, 1, 37, 2]
min = list_1[0]
for number in list_1:
    if number <min:
        min = number
list_2 =[i for i in list_1 if i > min]
second_small = list_2[0]
for number in list_2:
    if number < second_small:
        second_small = number
print(second_small)

