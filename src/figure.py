from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.area + other_figure.area
        else:
            raise ValueError('Can add only other figure')
