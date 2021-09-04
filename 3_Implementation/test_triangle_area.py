"""
Test trangle class
"""

from triangle_area import *

triangle_obj = Triangle(5, 5, 3, 10, 12)


def test_area_by_side():
    """
    Test area by side
    """
    assert triangle_obj.area_by_side() == 7.1545440106270926

def test_area_by_height_base():
    """
    Test area by Ht Base
    """
    assert triangle_obj.area_by_height_base() == 60
