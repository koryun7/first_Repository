# 3.Factorial
# Write a Python to calculate the factorial of a number
# (a non-negative integer). The function accepts the number argument.
def factorial(num):
    factorial_num = 1
    if num >= 0:
        for i in range(num):
            factorial_num *= num
            num -= 1
        return factorial_num


print(factorial(5))
