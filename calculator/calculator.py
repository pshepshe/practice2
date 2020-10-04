class Calculator:

    def __setattr__(self, key, value):
        if len(self.__dict__) == 10:
            return print('error: limit of attributes')
        else:
            self.__dict__[key] = value

    def __init__(self, start_number):
        self.value = start_number
        self.max_attribute = 10

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value + other)
        elif isinstance(other, Calculator):
            return Calculator(self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value - other)
        elif isinstance(other, Calculator):
            return Calculator(self.value - other.value)

    def __div__(self, other):
        if isinstance(other, (int, float)):
            return Calculator(self.value / other)
        elif isinstance(other, Calculator):
            return Calculator(self.value / other.value)

    def __pow__(self, power, modulo=None):
        if isinstance(power, (int, float)):
            return Calculator(self.value ** power)
        elif isinstance(power, Calculator):
            return Calculator(self.value ** power.value)

    def __str__(self):
        return str(self.__dict__.keys())


calc = Calculator(4)
calc2 = Calculator(2)
print((calc ** calc2 + 3/2*3 - 12 + 32 - calc2).value)
calc.property = 2
print(calc)

