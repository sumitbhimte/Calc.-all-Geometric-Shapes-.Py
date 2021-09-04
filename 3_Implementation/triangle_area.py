"""
File to claculated Triangle Area
"""
from math import sqrt


class Triangle:
    """
    Calculated Area and Perimeter of Triangle
    """
    def __init__(self, side1: float, side2: float, side3: float, height: float, base: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height
        self.base = base

    def area_by_side(self):
        """
        Calculated area by side
        """
        # calculate the semi-perimeter
        sumofsides = (self.side1 + self.side2 + self.side3) / 2

        return sqrt(sumofsides * (sumofsides - self.side1) * (sumofsides - self.side2) * (sumofsides - self.side3))

    def area_by_height_base(self):
        """
        Claculated area by Height & base
        """
        return 0.5 * self.height * self.base
