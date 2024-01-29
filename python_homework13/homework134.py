# Write a python program to find intersection
# of two given arrays using Lambda.
my_list1 = [1, 2, 3, 5, 7, 8, 9, 10]
my_list2 = [1, 2, 4, 8, 9]
intersection = list(filter(lambda x: x in my_list1, my_list2))
print(intersection)
