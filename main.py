from two_d_point import *
from rectangle import *
from quadrilateral import *
from square import *
from sorter import *


def main():
    point1 = TwoDPoint(2, 3)
    point2 = TwoDPoint(1, 3)
    point3 = TwoDPoint(1, 0)
    point4 = TwoDPoint(2, 0)
    rect = Rectangle(2, 3, 1, 3, 1, 0, 2, 0)
    rect1 = Rectangle(-2, 5, -2, 0, 5, 5, 5, 0)
    quad = Quadrilateral(1, 2, 3, 6, 10, 22, 8, 10)
    sqr = Square(4, 4, 2, 4, 2, 2, 4, 2)
    print(ShapeSorter.sort([rect, rect1, sqr, quad]))


if __name__ == '__main__':
    main()
