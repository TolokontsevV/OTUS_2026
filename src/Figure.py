from abc import ABC, abstractmethod


class Figure (ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        try:
            result = self.get_area + other_figure.get_area
            return result
        except Exception:
            raise ValueError('Can add only other_figure')
