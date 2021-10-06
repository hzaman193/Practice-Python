class Calculator3:
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
class SuperCalculator(Calculator3):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def square(self):
        return self.c * self.c

    def cube(self):
        return self.a * self.a * self.a
my_calculator = SuperCalculator(45,84,10)
print(my_calculator.square())
print(my_calculator.addition())








