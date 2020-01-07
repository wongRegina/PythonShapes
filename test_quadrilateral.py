from unittest import TestCase
from quadrilateral import *


class TestQuadrilateral(TestCase):

    def test_side_lengths_square(self):
        self.assertTrue((1, 1, 1, 1), Quadrilateral.side_lengths(Quadrilateral(1, 1, 0, 1, 0, 0, 1, 0)))

    def test_side_lengths_rectangle(self):
        self.assertTrue((1, 3, 1, 3), Quadrilateral.side_lengths(Quadrilateral(3, 1, 3, 0, 0, 0, 0, 3)))

    def test_side_lengths_trapezoid(self):
        self.assertTrue((3, math.sqrt(2), 5, math.sqrt(2)),
                        Quadrilateral.side_lengths(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0)))

    def test_side_lengths_false(self):
        self.assertFalse((), Quadrilateral.side_lengths(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0)))

    def test_smallest_x(self):
        self.assertEqual(0, Quadrilateral.smallest_x(Quadrilateral(1, 1, 0, 1, 0, 0, 1, 0)))

    def test_smallest_x(self):
        self.assertEqual(-1, Quadrilateral.smallest_x(Quadrilateral(0, 1, -1, 0, 0, -1, 1, 0)))

    def test_eq_true(self):
        self.assertTrue(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0) == (Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0)))

    def test_eq_false(self):
        self.assertFalse(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0) == (Quadrilateral(1, 1, 0, 1, 0, 0, 1, 0)))

    def test_neq_false(self):
        self.assertFalse(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0) != (Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0)))

    def test_eq_true(self):
        self.assertTrue(Quadrilateral(4, 1, 1, 1, 0, 0, 5, 0) != (Quadrilateral(1, 1, 0, 1, 0, 0, 1, 0)))

    def test_str(self):
        self.assertEqual('(%g, %g), (%g, %g), (%g, %g), (%g, %g)' % (1, 1, 1, 1, 1, 1, 1, 1),
                         Quadrilateral.__str__(Quadrilateral(1, 1, 1, 1, 1, 1, 1, 1)))
