from src.circle import Circle


def test_area(check_circle):
    a = 10
    c = Circle(a)
    assert c.area == 314.1592653589793


def test_perimeter(check_circle):
    a = 10
    c = Circle(a)
    assert c.perimeter == 62.83185307179586
