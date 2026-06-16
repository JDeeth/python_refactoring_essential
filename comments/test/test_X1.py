import unittest

from comments.src.X1 import Maths


class TestX1(unittest.TestCase):

    def test_n_basic(self):
        self.assertEqual(Maths.square(0), 0)
        self.assertEqual(Maths.square(2), 4)
        self.assertEqual(Maths.square(-3), 9)

    def test_m_single_value(self):
        self.assertEqual(Maths.sum_squares_of_range(3, 3), 9)

    def test_m_small_range(self):
        self.assertEqual(Maths.sum_squares_of_range(1, 3), 14)

    def test_m_larger_range(self):
        self.assertEqual(Maths.sum_squares_of_range(0, 3), 14)

    def test_m_negative_range(self):
        self.assertEqual(Maths.sum_squares_of_range(-2, 0), 5)

    def test_m_larger_negative_to_positive(self):
        self.assertEqual(Maths.sum_squares_of_range(-1, 1), 2)


if __name__ == "__main__":
    unittest.main()
