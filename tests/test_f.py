import unittest
import nod

class TestNod(unittest.TestCase):

    def test_nod1(self):
        gcd = nod.nod(35, 21)
        self.assertEqual(7, gcd, f"Expected 7 got {gcd}")

    def test_nod2(self):
        gcd = nod.nod(23,11)
        self.assertEqual(1, gcd, f"Expected 7 got {gcd}")

    def test_nod3(self):
        with self.assertRaises(ZeroDivisionError):
            gcd = nod.nod(0,11)
    
    def test_nod4(self):
        with self.assertRaises(ZeroDivisionError):
            gcd = nod.nod(11,0)

    def test_nod5(self):
        with self.assertRaises(TypeError):
            gcd = nod.nod('1', 3)
    
    def test_nod6(self):
        with self.assertRaises(TypeError):
            gcd = nod.nod(1, '3')


if __name__ == "__main__":
    unittest.main()