import math
from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError(f' Object of class Triangle must have sizes above 0, actual size is {a}/ {b}/ {c}')
        self.a = a
        self.b = b
        self.c = c

        if a + b < c or a + c < b or b + c < a:
            raise ValueError(f' With this sizes make triangle is impossible: {a}/ {b}/ {c}')

    @property
    def get_perimeter(self):
        return self.a + self.b + self.c

    @property
    def get_area(self):
        return math.sqrt(self.get_perimeter/2 * (self.get_perimeter/2 - self.a) * (self.get_perimeter/2 - self.b) * (self.get_perimeter/2 - self.c))  # рассчет по формуле Герона
