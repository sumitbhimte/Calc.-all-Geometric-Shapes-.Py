from triangleArea import *

triangle_obj = triangle(5, 5, 3, 10, 12)


def test_area_by_side():
    assert  7.1545440106270926  == triangle_obj.area_by_side()

def test_areaByHeightBase():
    assert 60 ==triangle_obj.areaByHeightBase()
