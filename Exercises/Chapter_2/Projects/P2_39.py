from abc import ABCMeta, abstractmethod
from math import tan

class Polygon(metaclass=ABCMeta):
    def __init__(self, length, num_side):
        self._length = length
        self._num_side = num_side

    @abstractmethod
    def get_area(self):
        """ Returns area """

    @abstractmethod
    def get_perimeter(self):
        """ Returns perimeter """

    def get_properties(self):
        return ('Perimeter: ' + str(self.get_perimeter()) +
                ' Area: ' + str(self.get_area()))

class Triangle(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=3)

    def get_area(self):
        return self._length * self._length / 2

    def get_perimeter(self):
        return self._length * self._num_side

class Quadrilateral(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=4)

    def get_area(self):
        return self._length * self._length

    def get_perimeter(self):
        return self._length * self._num_side

class Pentagon(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=5)

    def get_area(self):
        return .25 * pow(5 * (5 + 2*pow(5,.5)), .5) * pow(self._length,2)

    def get_perimeter(self):
        return self._length * self._num_side

class Hexagon(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=6)

    def get_area(self):
        return 3 * pow(3, .5) * pow(self._length, 2) / 2

    def get_perimeter(self):
        return self._length * self._num_side

class Octagon(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=8)

    def get_area(self):
        return 2*(1 + pow(2,.5)) * pow(self._length, 2)

    def get_perimeter(self):
        return self._length * self._num_side

class IsoscelesTriangle(Polygon):
    def __init__(self, base, height):
        super().__init__(base, num_side=3)
        self._base = base
        self._height = height

    def get_area(self):
        return .5 * self._base * self._height

    def get_perimeter(self):
        return 2 * self._height + self._base

class EquilateralTriangle(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=3)

    def get_area(self):
        return pow(3, .5)/4 * pow(self._length, 2)

    def get_perimeter(self):
        return self._length * self._num_side

class Rectangle(Polygon):
    def __init__(self, height, width):
        super().__init__(height, num_side=4)
        self._height = height
        self._width = width

    def get_area(self):
        return self._height * self._width

    def get_perimeter(self):
        return 2 * self._height + 2 * self._width

class Square(Polygon):
    def __init__(self, length):
        super().__init__(length, num_side=4)

    def get_area(self):
        return self._length * self._length

    def get_perimeter(self):
        return self._length * self._num_side

if __name__ == '__main__':
    triangle = Triangle(4)
    quad = Quadrilateral(5)
    pent = Pentagon(6)
    hexa = Hexagon(7)
    octa = Octagon(8)
    iso_tri = IsoscelesTriangle(9, 10)
    eq_tri = EquilateralTriangle(11)
    rect = Rectangle(12, 13)
    square = Square(14)

    shapes = []
    shapes.append(triangle)
    shapes.append(quad)
    shapes.append(pent)
    shapes.append(hexa)
    shapes.append(octa)
    shapes.append(iso_tri)
    shapes.append(eq_tri)
    shapes.append(rect)
    shapes.append(square)

    for shape in shapes:
        print(type(shape).__name__)
        print(shape.get_properties())
