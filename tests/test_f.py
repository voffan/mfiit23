import unittest
import factor

class TestF(unittest.TestCase):

    def test_f1(self):
        result = factor.factor(12)
        self.assertEqual(isinstance(result, dict), True, "Result is not Dict!")
        self.assertEqual(result[2], 2, "Power of 2 is not 2!")
        self.assertEqual(result[3], 1, "Power of 3 is not 1!")

    def test_f2(self):
        with self.assertRaises(TypeError):
            factor.factor(12.5)

    def test_f3(self):
        with self.assertRaises(Exception):
            factor.factor(-5)

    def test_f4(self):
        result = factor.factor(2)
        self.assertEqual(isinstance(result, dict), True)
        self.assertEqual(result[2], 1, "Power of 1 must be 1!")

    def test_f5(self):
        with self.assertRaises(Exception):
            factor.factor(1)

    def test_f6(self):
        with self.assertRaises(Exception):
            factor.factor(0)