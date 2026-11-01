from src.square import Square
import pytest


@pytest.mark.regress
def test_area():
    a = 10
    s = Square(a)
    assert s.area == 100


@pytest.mark.regress
@pytest.mark.last
def test_perimeter():
    a = 10
    s = Square(a)
    assert s.perimeter == 40
