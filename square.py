import math

from two_d_point import TwoDPoint
from rectangle import Rectangle
from quadrilateral import Quadrilateral


class Square(Rectangle):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def __eq__(self, other) -> bool:
        if isinstance(other, self.__class__):
            return self.vertices == other.vertices
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '(%g, %g), (%g, %g), (%g, %g), (%g, %g)' % (
            self.vertices[0].x, self.vertices[0].y, self.vertices[1].x, self.vertices[1].y,
            self.vertices[2].x, self.vertices[2].y, self.vertices[3].x, self.vertices[3].y)

    def __is_member(self) -> bool:
        side_lengths = super().side_lengths()
        if side_lengths[0] != side_lengths[1] or side_lengths[1] != side_lengths[2] or side_lengths[0] != side_lengths[2]:
            return False
        if (self.vertices[0].x - self.vertices[1].x) != 0:
            slope1 = ((self.vertices[0].y - self.vertices[1].y) / (self.vertices[0].x - self.vertices[1].x))
        else:
            slope1 = 0
        if (self.vertices[2].x - self.vertices[1].x) != 0:
            slope2 = ((self.vertices[2].y - self.vertices[1].y) / (self.vertices[2].x - self.vertices[1].x))
        else:
            slope2 = 0
        if slope1 == 0 or slope2 == 0:
            return (slope1 + slope2) != 1
        if slope1 != - 1 / slope2:
            return False
        return True  # TODO

    def snap(self) -> 'TwoDPoint':
        """Snaps the sides of the square such that each corner (x,y) is modified to be a corner (x',y') where x' is the
        integer value closest to x and y' is the integer value closest to y. This, of course, may change the shape to a
        general quadrilateral, hence the return type. The only exception is when the square is positioned in a way where
        this approximation will lead it to vanish into a single point. In that case, a call to snap() will not modify
        this square in any way."""
        vertices = self.vertices
        point0 = TwoDPoint(int(round(vertices[0].x)), int(round(vertices[0].y)))
        point1 = TwoDPoint(int(round(vertices[1].x)), int(round(vertices[1].y)))
        if point0 == point1:
            return self
        return Quadrilateral(int(round(vertices[0].x)), int(round(vertices[0].y)), int(round(vertices[1].x)),
                             int(round(vertices[1].y)), int(round(vertices[2].x)), int(round(vertices[2].y)),
                             int(round(vertices[3].x)), int(round(vertices[3].y)))  # TODO
