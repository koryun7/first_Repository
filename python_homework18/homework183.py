# List Exercise:
# Given a list of numbers, write a function to find the sum of all numbers in the list that
# can be divided by 7.
def divisible_seven(nums):
    divisible = [num for num in nums if num % 7 == 0]

    return divisible


numbers = [14, 21, 30, 42, 56, 63, 70, 88, 91]

result = divisible_seven(numbers)
print(result)