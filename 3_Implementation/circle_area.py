"""
This is circle Class to claculate area and perimeter
"""
from math import pi


class Circle:
    """
    Class Circle
    """
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """
        Circle Area Claculated
        """
        return pi * self.radius * self.radius

    def perimeter(self):
        """
        Circle Perimeter Calculated
        """
        return 2 * pi * self.radius
