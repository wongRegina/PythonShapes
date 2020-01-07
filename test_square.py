from unittest import TestCase
from square import *


class TestSquare(TestCase):

    def test_isMember_not_valid(self):
        with self.assertRaises(Exception):
            Square(3, 1, 3, 0, 0, 0, 0, 3)

    def test_isMember_valid(self):
        try:
            Square(1, 1, 0, 1, 0, 0, 1, 0)
        except Exception:
            self.assertFalse(True)

    def test_eq_true(self):
        self.assertTrue(Square(1, 1, 0, 1, 0, 0, 1, 0) == Square(1, 1, 0, 1, 0, 0, 1, 0))

    def test_eq_false(self):
        self.assertFalse(Square(2, 2, 0, 2, 0, 0, 2, 0) == Square(1, 1, 0, 1, 0, 0, 1, 0))

    def test_neq_false(self):
        self.assertFalse(Square(1, 1, 0, 1, 0, 0, 1, 0) != Square(1, 1, 0, 1, 0, 0, 1, 0))

    def test_neq_true(self):
        self.assertTrue(Square(2, 2, 0, 2, 0, 0, 2, 0) != Square(1, 1, 0, 1, 0, 0, 1, 0))

    def test_str(self):
        self.assertEqual('(%g, %g), (%g, %g), (%g, %g), (%g, %g)' % (1, 1, 0, 1, 0, 0, 1, 0),
                         Square.__str__(Square(1, 1, 0, 1, 0, 0, 1, 0)))

    def test_snap_new_quad(self):
        self.assertEqual(
            Quadrilateral(8, 4, 4, 4, 4, 0, 8, 0), Square.snap(Square(7.7, 4.2, 3.5, 4.2, 3.5, 0, 7.7, 0)))

    def test_snap_same_square(self):
        self.assertEqual(
            Square(0.45, 0.45, 0, 0.45, 0, 0, 0.45, 0), Square.snap(Square(0.45, 0.45, 0, 0.45, 0, 0, 0.45, 0)))
