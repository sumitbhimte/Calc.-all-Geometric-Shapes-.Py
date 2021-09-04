import circleArea
from circleArea import *

circle_obj = circle(3)


def test_area():
    assert 28.274333882308138 == circle_obj.area()


def test_perimeter():
    assert 18.84955592153876 == circle_obj.perimeter()
