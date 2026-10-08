from src.rectangle import Rectangle
from src.circle import Circle
from src.square import Square
from src.triangle import Triangle


if __name__ == '__main__':
    try:
        t = Triangle(1, 2, 4)
        c = Circle(10)
        r = Rectangle(10, 12)
        s = Square(10)

        print(t.area)
        print(c.area)
        print(t.add_area(c))
    except ValueError as error:
        print(error)
