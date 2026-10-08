from src.circle import Circle


def test_circle_area(check_circle):
    c = Circle(10)
    assert c.area == 314.1592653589793


def test_circle_perimeter(check_circle):
    c = Circle(10)
    assert c.perimeter == 62.83185307179586
