import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        if a <= 0 or b <= 0 or c <= 0 or a + b == c:
            raise ValueError(f" a, b, c, must be positive, actual sizes is {a}/{b}/{c}, or sum of two sides equals to other side")
        self.a = a
        self.b = b
        self.c = c

        if a + b < c or a + c < b or b + c < a:
            raise ValueError(f" with this sizes make triangle is impossible, actual sizes is {a}/{b}/{c}")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return math.sqrt(self.perimeter/2 * (self.perimeter/2 - self.a) * (self.perimeter/2 - self.b) * (self.perimeter/2 - self.c))  # расчет по формуле Герона
