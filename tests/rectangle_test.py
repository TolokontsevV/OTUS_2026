from src.rectangle import Rectangle
import pytest


a = 8
b = 20


@pytest.mark.skipif(condition=a == 10 or b == 16, reason="not implemented")
def test_rectangle_area():
    r = Rectangle(a, b)
    assert r.area == 160


@pytest.mark.parametrize(
    ('side_a', 'side_b', 'perimeter'),
    [
        pytest.param(10, 15, 50, id='integer'),
        pytest.param(10.6, 20.4, 62.0, id='float'),
    ]
)
def test_rectangle_perimeter(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == perimeter
