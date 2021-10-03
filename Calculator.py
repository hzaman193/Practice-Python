class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            return self.a / self.b

        except ZeroDivisionError:
            return 'It is impossible to divided by Zero'


myCalculator = Calculator(36,2)
tmp = myCalculator.addition()
print(f"Addition is {tmp}")
tmp = myCalculator.addition()
print(f"Subtraction is {tmp}")
tmp = myCalculator.addition()
print(f"Multiplication is {tmp}")
tmp = myCalculator.addition()
print(f"Division is {tmp}")

