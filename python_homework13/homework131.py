# Write a Python program to square and cube every number in a given list of
# integers using Lambda.
square = lambda x: x ** 2
cube = lambda x: x ** 3
numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(square, numbers))
cube_numbers = list(map(cube, numbers))
print(square_numbers)
print(cube_numbers)
