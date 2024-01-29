# 1.Max of three
# Write a Python function to find the Max of three numbers.
def max_of_three(num1, num2, num3):
    result = 0
    for i in num1, num2, num3:
        if i > result:
            result = i
    return result


print(max_of_three(5, 11, 3))
