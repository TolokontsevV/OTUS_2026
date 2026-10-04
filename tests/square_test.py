from src.square import Square
import pytest

a = 10


@pytest.mark.regress
def test_rectangle_area():
    s = Square(a)
    assert s.area == 100


@pytest.mark.regress
@pytest.mark.last
def test_rectangle_perimeter():
    s = Square(a)
    assert s.perimeter == 40
