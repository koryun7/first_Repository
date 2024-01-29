# Math Operations Exercise:
# Write a function that calculates the square root of a number using the math module.
import math

def calculate_square_root(number):
    if number < 0:
        return "Հնարավոր չէ հաշվել բացասական թվի քառակուսի արմատը"
    else:
        return math.sqrt(number)


input_number = 25

result = calculate_square_root(input_number)
print(f"{input_number}-ի քառակուսի արմատը {result}")

