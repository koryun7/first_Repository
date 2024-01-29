#Write a Python program to remove duplicates from a list
list = [25, 25, 1, 2, 1, 13]
result = []
for item in list:
    if item not in result:
        result.append(item)

print(result)