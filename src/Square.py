from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        super().__init__()
        if a <= 0:
            raise ValueError(f' Object of class Square must have size above 0, actual size is {a}')
        self.a = a

    @property
    def get_perimeter(self):
        return self.a * 4

    @property
    def get_area(self):
        return self.a ** 2
