from unittest import TestCase
from rectangle import *
from quadrilateral import *
from square import *
from sorter import *


class TestShapeSorter(TestCase):

    def test_sorted_notSorted(self):
        rect = Rectangle(2, 3, 1, 3, 1, 0, 2, 0)
        rect1 = Rectangle(-2, 5, -2, 0, 5, 5, 5, 0)
        quad = Quadrilateral(1, 2, 3, 6, 10, 22, 8, 10)
        sqr = Square(4, 4, 2, 4, 2, 2, 4, 2)
        self.assertTrue([rect1, rect, quad, sqr] == ShapeSorter.sort([rect, rect1, sqr, quad]))

    def test_sorted_empty(self):
        self.assertTrue([] == ShapeSorter.sort([]))

    def test_sorted_oneValue(self):
        rect = Rectangle(2, 3, 1, 3, 1, 0, 2, 0)
        self.assertTrue([rect] == ShapeSorter.sort([rect]))

    def test_sort_sorted(self):
        rect = Rectangle(2, 3, 1, 3, 1, 0, 2, 0)
        rect1 = Rectangle(-2, 5, -2, 0, 5, 5, 5, 0)
        quad = Quadrilateral(1, 2, 3, 6, 10, 22, 8, 10)
        sqr = Square(4, 4, 2, 4, 2, 2, 4, 2)
        self.assertTrue([rect1, rect, quad, sqr] == ShapeSorter.sort([rect1, rect, quad, sqr]))
