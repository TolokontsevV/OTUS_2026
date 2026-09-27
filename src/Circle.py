import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, a):
        super().__init__()
        if a <= 0:
            raise ValueError(f' Object of class Circle must have radius above 0, actual radius is {a}')
        self.a = a

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.a

    @property
    def get_area(self):
        return math.pi * self.a ** 2
