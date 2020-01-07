from unittest import TestCase
from two_d_point import TwoDPoint


class TestTwoDPoint(TestCase):

    def test_from_coordinates_odd(self):
        # Odd values
        with self.assertRaises(Exception):
            TwoDPoint.from_coordinates([1, 1, 0, 0, 3])

    def test_from_coordinates_even(self):
        # Even values
        self.assertEqual([TwoDPoint(1, 1), TwoDPoint(0, 0)], TwoDPoint.from_coordinates([1, 1, 0, 0]))

    def test_from_coordinates_zero(self):
        # zero
        self.assertEqual([], TwoDPoint.from_coordinates([]))

    def test_from_coordinates_decimal_odd(self):
        # Odd values (decimal)
        with self.assertRaises(Exception):
            TwoDPoint.from_coordinates([1.4, 1.9, 0.5, -0.5, 3.0])

    def test_from_coordinates_decimal_even(self):
        # Even values (decimal)
        self.assertEqual([TwoDPoint(1.4, 1.9), TwoDPoint(0.5, -0.5), TwoDPoint(3.0, -1)],
                         TwoDPoint.from_coordinates([1.4, 1.9, 0.5, -0.5, 3.0, -1]))

    def test_eq_false(self):
        self.assertFalse((TwoDPoint(1, 1) == TwoDPoint(1, 3)))

    def test_eq_true(self):
        self.assertTrue(TwoDPoint(1, 1) == TwoDPoint(1, 1))

    def test_neq_true(self):
        self.assertTrue((TwoDPoint(1, 1) != TwoDPoint(1, 3)))

    def test_neq_false(self):
        self.assertFalse(TwoDPoint(1, 1) != TwoDPoint(1, 1))

    def test_add_true(self):
        self.assertTrue(TwoDPoint(3, 3) == (TwoDPoint(1, 1) + TwoDPoint(2, 2)))

    def test_add_false(self):
        self.assertFalse(TwoDPoint(3, 5) == (TwoDPoint(6, 1) + TwoDPoint(2, 2)))

    def test_sub_true(self):
        self.assertTrue(TwoDPoint(5, 2) == (TwoDPoint(8, 7) - TwoDPoint(3, 5)))

    def test_sub_false(self):
        self.assertFalse(TwoDPoint(9, 2) == (TwoDPoint(3, 7) - TwoDPoint(3, 5)))

    def test_str(self):
        self.assertEqual('(%g, %g)' % (1, 1), TwoDPoint.__str__(TwoDPoint(1, 1)))
