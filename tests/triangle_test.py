from src.triangle import Triangle
import pytest


a = 2
b = 4
c = 5


@pytest.fixture
def start_error():
    print('\n Start check error')
    yield
    print('\n End check error')


def test_error_above_0(start_error):
    if a <= 0 or b <= 0 or c <= 0 or a + b == c:
        raise ValueError(
            f" a, b, c, must be positive, actual sizes is {a}/{b}/{c}, or sum of two sides equals to other side")


def test_error_triangle_possibility(start_error):
    if a + b < c or a + c < b or b + c < a:
        raise ValueError(f" with this sizes make triangle is impossible, actual sizes is {a}/{b}/{c}")

# не смог сделать так что бы тесты на проверку area и perimeter, запускались только в том случае,
# если пройдены тесты на ValueError. Пытался использовать методы с использованием skipif при разделении
# тестов между собой фикстурами, через if/else в когда тесты под одной фикстурой


def start_triangle():
    print('\n Start triangle')

    yield

    print('\n end triangle')


def test_triangle_area(start_error):
    t = Triangle(a, b, c)
    assert t.area == 3.799671038392666


def test_triangle_perimeter(start_error):
    t = Triangle(a, b, c)
    assert t.perimeter == 11
