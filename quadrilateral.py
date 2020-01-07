import math

from two_d_point import TwoDPoint
from typing import Tuple


class Quadrilateral:

    def __init__(self, *floats):
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.vertices == other.vertices
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '(%g, %g), (%g, %g), (%g, %g), (%g, %g)' % (
            self.__vertices[0].x, self.__vertices[0].y, self.__vertices[1].x, self.__vertices[1].y,
            self.__vertices[2].x, self.__vertices[2].y, self.__vertices[3].x, self.__vertices[3].y)

    @property
    def vertices(self):
        return self.__vertices

    def side_lengths(self) -> Tuple:
        """Returns a tuple of four floats, each denoting the length of a side of this quadrilateral. The value must be
        ordered clockwise, starting from the top left corner."""
        dist1 = math.sqrt(
            (self.vertices[0].x - self.vertices[1].x) ** 2 + (self.vertices[0].y - self.vertices[1].y) ** 2)
        dist2 = math.sqrt(
            (self.vertices[2].x - self.vertices[1].x) ** 2 + (self.vertices[2].y - self.vertices[1].y) ** 2)
        dist3 = math.sqrt(
            (self.vertices[2].x - self.vertices[3].x) ** 2 + (self.vertices[2].y - self.vertices[3].y) ** 2)
        dist4 = math.sqrt(
            (self.vertices[0].x - self.vertices[3].x) ** 2 + (self.vertices[0].y - self.vertices[3].y) ** 2)
        return dist1, dist2, dist3, dist4  # TODO

    def smallest_x(self) -> Tuple:
        """Returns the x-coordinate of the vertex with the smallest x-value of the four vertices of this
        quadrilateral."""
        x0 = self.vertices[0].x
        x1 = self.vertices[1].x
        x2 = self.vertices[2].x
        x3 = self.vertices[3].x
        return min(x0, x1, x2, x3)  # TODO
