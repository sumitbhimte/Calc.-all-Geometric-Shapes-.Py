from math import tan, pi

class Rectangle:
    def __init__(self, width: float, height: float):
        self.height = height
        self.width = width

    def set_width(self, width: float):
        """set width of rectangle"""
        self.width = width

    def set_height(self, height: float):
        """set height of rectangle"""
        self.height = height

    def get_area(self):
        """Returns area (width * height)"""
        return self.width * self.height

    def get_perimeter(self):
        """Returns perimeter (2 * width + 2 * height)"""
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Returns diagonal ((width ** 2 + height ** 2) ** .5)"""
        return (self.width ** 2 + self.height ** 2) ** .5


class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side: float):
        """set side length of the square"""
        self.side = side
        self.set_width = side
        self.set_height = side


class parallelogram(Rectangle):
    def __init__(self, base: float, height: float):
        super().__init__(base,height )
        self.base = base
        self.height = height

    def set_param(self, base: float,  height: float):
        """set side length of the square"""
        self.set_width = base
        self.set_height = height


class reg_polygon(Rectangle):
    def __init__(self,n_sides: float,n_length: float):
        self.n_sides = n_sides
        self.n_length = n_length

    def get_area(self):
        return self.n_sides * (self.n_length ** 2) / (4 * tan(pi / self.n_sides))

    def get_perimeter(self):
        return self.n_sides*self.n_length

