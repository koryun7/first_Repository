# Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.
class BasicCalculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Չի կարող բաժանել զրոյի"


calculator = BasicCalculator()
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(10, 7)
result_multiply = calculator.multiply(3, 4)
result_divide = calculator.divide(8, 2)

print(result_add)
print(result_subtract)
print(result_multiply)
print(result_divide)