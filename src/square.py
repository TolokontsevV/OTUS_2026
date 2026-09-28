from src.figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        if a <= 0:
            raise ValueError(f" a must be positive, actual sizes is {a}")
        self.a = a

    @property
    def get_perimeter(self):
        return self.a * 4

    @property
    def get_area(self):
        return self.a ** 2
