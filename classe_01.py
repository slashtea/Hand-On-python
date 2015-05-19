__author__ = 'shannon'


class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        added = self.x + self.y
        print(added)

    def substraction(self):
        sub = self.x - self.y
        print(sub)

    def multiplication(self):
        mult = self.x * self.y
        print(mult)

    def division(self):
        div = self.x / self.y
        print(div)

c = Calculator(3, 5)
c.addition()