import unittest
import Fraction


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.fraction1 = Fraction.Fraction(3, 4)

        # 1. create a fraction2 object with numerator 2 and denominator 3
        self.fraction2 = Fraction.Fraction(2, 3)

        # 2. create a fraction3 object with numerator 1 and denominator 4
        self.fraction3 = Fraction.Fraction(1, 4)

    def test_instance_creation(self):
        self.assertIsInstance(self.fraction1, Fraction.Fraction)

    def test_instance_creation_0Denom(self):
        self.assertRaises(ValueError, Fraction.Fraction, 1, 0)

    def test_get_numerator(self):
        self.assertEquals(self.fraction1.get_numerator(), 3)

    def test_get_denominator(self):
        # 3. create a test to check the denominator of the self.fraction1 object
        self.assertEqual(4, self.fraction1.get_denominator())

    def test_set_denominatorBasic(self):
        self.fraction1.set_denominator(8)
        self.assertEquals(self.fraction1.__str__(), "3/8")

    def test_set_denominator0(self):
        # 4. test that setting the denominator of self.fraction1 raises a ValueError
        self.assertRaises(ValueError, self.fraction1.set_denominator(0))

    def test_str(self):
        self.assertEquals(self.fraction1.__str__(), "3/4")

    def test_add(self):
        self.fraction1.add(self.fraction2)
        self.assertEquals(self.fraction1.__str__(), "17/12")

    def test_add_reduce(self):
        self.fraction3.add(self.fraction3)
        self.assertEquals(self.fraction3.__str__(), "1/2")

    def test_subtract(self):
        # 5. test self.fraction1 - self.fraction2
        self.fraction1.subtract(self.fraction2)
        self.assertEqual(self.fraction1.__str__(), "1/12")

    def test_subtract_reduce(self):
        self.fraction1.subtract(self.fraction3)
        self.assertEquals(self.fraction1.__str__(), "1/2")

    def test_multiply(self):
        # 6. test the multiply method, checking fraction1 * fraction2
        self.fraction1.multiply(self.fraction2)
        self.assertEqual(self.fraction1.__str__(), "1/2")


if __name__ == '__main__':
    unittest.main()


