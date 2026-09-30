from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__()
        if a <= 0 or b <= 0:
            raise ValueError(f" a, b must be positive, actual sizes is {a}/{b}")
        self.a = a
        self.b = b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
