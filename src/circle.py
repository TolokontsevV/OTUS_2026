import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, a):
        super().__init__()
        if a <= 0:
            raise ValueError(f" a must be positive, actual sizes is {a}")
        self.a = a

    @property
    def perimeter(self):
        return 2 * math.pi * self.a

    @property
    def area(self):
        return math.pi * self.a ** 2
