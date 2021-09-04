from shape_calculator import *

rectangle_obj = Rectangle(5,10)

def test_rectangle_area():
    assert rectangle_obj.get_area() == 50

def test_rectangle_perimeter():
    assert rectangle_obj.get_perimeter() ==30

def test_rectangle_diagonal():
    assert rectangle_obj.get_diagonal() ==11.180339887498949


square_obj =Square(9)


def test_square_area():
    assert square_obj.get_area() == 81


def test_square_perimeter():
    assert square_obj.get_perimeter() == 36


def test_square_diagonal():
    assert square_obj.get_diagonal() == 12.727922061357855

parallelogram_obj = parallelogram(5,5)

def test_parallelogram_area():
    assert parallelogram_obj.get_area() == 25


def test_parallelogram_perimeter():
    assert parallelogram_obj.get_perimeter() == 20
