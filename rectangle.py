import math

from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats):
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

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
        """Returns True if the given coordinates form a valid rectangle, and False otherwise."""
        side_lengths = super().side_lengths()
        if side_lengths[0] != side_lengths[2] or side_lengths[1] != side_lengths[3]:
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

    def center(self) -> 'TwoDPoint':
        """Returns the center of this rectangle, calculated to be the point of intersection of its diagonals."""
        return TwoDPoint((self.vertices[0].x + self.vertices[2].x) / 2,
                         (self.vertices[0].y + self.vertices[2].y) / 2)  # TODO

    def area(self) -> float:
        """Returns the area of this rectangle. The implementation invokes the side_lengths() method from the superclass,
        and computes the product of this rectangle's length and width."""
        side_lengths = super().side_lengths()
        return side_lengths[0] * side_lengths[1]  # TODO
