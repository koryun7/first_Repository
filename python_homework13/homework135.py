# Write a Python program to add two given lists using map and
# lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
# ynduni, orinak erku list)
x = [1, 2, 3]
y = [4, 5, 6]
result = list(map(lambda x, y: x + y, x, y))
print(result)
