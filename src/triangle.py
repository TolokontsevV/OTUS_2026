import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def above_0(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0 or self.a + self.b == self.c:
            raise ValueError(f" a, b, c, must be positive, actual sizes is {self.a}/{self.b}/{self.c}, or sum of two sides equals to other side")

    def impossible_triangle(self):
        if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            raise ValueError(f" with this sizes make triangle is impossible, actual sizes is {self.a}/{self.b}/{self.c}")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return math.sqrt(self.perimeter/2 * (self.perimeter/2 - self.a) * (self.perimeter/2 - self.b) * (self.perimeter/2 - self.c))  # расчет по формуле Герона
