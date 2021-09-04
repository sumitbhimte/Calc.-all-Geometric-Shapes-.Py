"""
Test Recctangle Square and Parellalogram Functions
"""

from shape_calculator import *

rectangle_obj = Rectangle(5,10)

def test_rectangle_area():
    """
    Test Rectangel area
    """
    assert rectangle_obj.get_area() == 50

def test_rectangle_perimeter():
    """
    Test Rectangel perimeter
    """
    assert rectangle_obj.get_perimeter() == 30

def test_rectangle_diagonal():
    """
    Test Rectangel Diagonal
    """
    assert rectangle_obj.get_diagonal() == 11.180339887498949


square_obj = Square(9)


def test_square_area():
    """
    Test Square area
    """
    assert square_obj.get_area() == 81


def test_square_perimeter():
    """
    Test Square Perimeter
    """
    assert square_obj.get_perimeter() == 36


def test_square_diagonal():
    """
    Test square Diagonal
    """
    assert square_obj.get_diagonal() == 12.727922061357855

parallelogram_obj = Parallelogram(5,5)

def test_parallelogram_area():
    """
    Test parallelogram_area
    """
    assert parallelogram_obj.get_area() == 25


def test_parallelogram_perimeter():
    """
    Test parallelogram Perimeter
    """
    assert parallelogram_obj.get_perimeter() == 20
