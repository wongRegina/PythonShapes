from unittest import TestCase
from rectangle import *


class TestRectangle(TestCase):

    def test_isMember_not_valid(self):
        with self.assertRaises(Exception):
            Rectangle(3, 1, 3, 0, 0, 0, 0, 3)

    def test_isMember_valid(self):
        try:
            Rectangle(3, 1, 0, 1, 0, 0, 3, 0)
        except Exception:
            self.assertFalse(True)

    def test_eq_true(self):
        self.assertTrue(Rectangle(3, 1, 0, 1, 0, 0, 3, 0) == Rectangle(3, 1, 0, 1, 0, 0, 3, 0))

    def test_eq_false(self):
        self.assertFalse(Rectangle(3, 1, 0, 1, 0, 0, 3, 0) == Rectangle(1, 1, 0, 1, 0, 0, 1, 0))

    def test_neq_false(self):
        self.assertFalse(Rectangle(3, 1, 0, 1, 0, 0, 3, 0) != Rectangle(3, 1, 0, 1, 0, 0, 3, 0))

    def test_eq_true(self):
        self.assertTrue(Rectangle(3, 1, 0, 1, 0, 0, 3, 0) != Rectangle(1, 1, 0, 1, 0, 0, 1, 0))

    def test_str(self):
        self.assertEqual('(%g, %g), (%g, %g), (%g, %g), (%g, %g)' % (3, 1, 0, 1, 0, 0, 3, 0),
                         Rectangle.__str__(Rectangle(3, 1, 0, 1, 0, 0, 3, 0)))

    def test_center(self):
        self.assertTrue(TwoDPoint(1.5, .5) == Rectangle.center(Rectangle(3, 1, 0, 1, 0, 0, 3, 0)))

    def test_area(self):
        self.assertEqual(3, Rectangle.area(Rectangle(3, 1, 0, 1, 0, 0, 3, 0)))
