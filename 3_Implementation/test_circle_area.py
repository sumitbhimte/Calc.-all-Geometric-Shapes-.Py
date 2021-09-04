"""
Test Circle Functions
"""
import circle_area
from circle_area import *

circle_obj = Circle(3)


def test_area():
    """
    Test Circle Area
    """
    assert circle_obj.area() == 28.274333882308138


def test_perimeter():
    """
    Test Circle Perimeter
    """
    assert circle_obj.perimeter() == 18.84955592153876
