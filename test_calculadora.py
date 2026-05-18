import unittest
from calculadora import multiply

class TestCalculadora(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(10, multiply(2, 5))

    def test_multiply_zero(self):
        self.assertEqual(0, multiply(0, 5))

    def test_multiply_negative(self):
        self.assertEqual(-6, multiply(-2, 3))

if __name__ == "__main__":
    unittest.main()