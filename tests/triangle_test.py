from src.triangle import Triangle
import pytest


@pytest.fixture
def start_error():
    print('\n Start check error')

    yield

    print('\n End check error')


def test_above_0(start_error):
    a = 5
    b = 5
    c = 10
    t = Triangle(a, b, c)
    with pytest.raises(ValueError):
        assert t.above_0()


def test_impossible_triangle(start_error):
    a = 6
    b = 14
    c = 7
    t = Triangle(a, b, c)
    with pytest.raises(ValueError):
        assert t.impossible_triangle()


@pytest.fixture
def start_triangle():
    print('\n Start triangle')

    yield

    print('\n end triangle')


def test_area(start_triangle):
    a = 2
    b = 4
    c = 5
    t = Triangle(a, b, c)
    assert t.area == 3.799671038392666


def test_perimeter(start_triangle):
    a = 2
    b = 4
    c = 5
    t = Triangle(a, b, c)
    assert t.perimeter == 11
