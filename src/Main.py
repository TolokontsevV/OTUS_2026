from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle
from src.Square import Square


if __name__ == '__main__':
    try:
        r = Rectangle(10, 12)
        t = Triangle(13, 14, 15)
        s = Square(10)
        c = Circle(15)
        s.add_area(c)
        print(s.get_area)
        print(t.get_area)
        print(s.add_area(t))
    except Exception as Error:
        print(Error)
