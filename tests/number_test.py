import unittest
import number

class TestRealNumber(unittest.TestCase):
	def test_denominator_getter(self):
		n1 = number.RealNumber(1/3)
		assert(n1.denominator == 3)

		n2 = number.RealNumber(2)
		assert(n2.denominator == 1)

		n3 = number.RealNumber(numerator=1, denominator=2)
		assert(n3.denominator == 2)

		n4 = number.RealNumber(1/2, as_fraction=False)
		assert(n4.denominator == None)

	def test_numerator_getter(self):
		n1 = number.RealNumber(1/3)
		assert(n1.numerator == 1)

		n2 = number.RealNumber(2)
		assert(n2.numerator == 2)

		n3 = number.RealNumber(numerator=3, denominator=2)
		assert(n3.numerator == 3)

		n4 = number.RealNumber(4/5, as_fraction=False)
		assert(n4.numerator == None)