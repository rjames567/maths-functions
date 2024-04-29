import decimal
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

	def test_denominator_setter(self):
		n1 = number.RealNumber(1/3)
		n1.denominator = 2
		assert(
			n1.denominator == 2 and 
			n1.numerator == 1 and 
			n1.exact_value == (1/2)
		)

		n2 = number.RealNumber(2)
		n2.denominator = 2
		assert(
			n2.denominator == 1 and
			n2.numerator == 1 and 
			n2.exact_value == 1
		)

		n3 = number.RealNumber(numerator=3, denominator=2)
		n3.denominator = 6
		assert(
			n3.denominator == 2 and
			n3.numerator == 1 and 
			n3.exact_value == (1/2)
		)

		def temp():
			n4 = number.RealNumber(4/5, as_fraction=False)
			n4.denominator = 2
		self.assertRaises(
			Exception,
			temp
		)

	def test_numerator_setter(self):
		n1 = number.RealNumber(1/3)
		n1.numerator = 2
		assert(
			n1.denominator == 3 and 
			n1.numerator == 2 and 
			n1.exact_value == (2/3)
		)
	
		n2 = number.RealNumber(2)
		n2.numerator = 4
		assert(
			n2.denominator == 1 and
			n2.numerator == 4 and 
			n2.exact_value == 4
		)
	
		n3 = number.RealNumber(numerator=3, denominator=4)
		n3.numerator = 2
		assert(
			n3.denominator == 2 and
			n3.numerator == 1 and 
			n3.exact_value == (1/2)
		)
	
		def temp():
			n4 = number.RealNumber(4/5, as_fraction=False)
			n4.numerator = 2
		self.assertRaises(
			Exception,
			temp
		)

	def test_exact_value_getter(self):
		n1 = number.RealNumber(1/3)
		assert(n1.exact_value == (1/3))

		n2 = number.RealNumber(2)
		assert(n2.exact_value == 2)

		n3 = number.RealNumber(numerator=3, denominator=4)
		assert(n3.exact_value == (3/4))

		n4 = number.RealNumber(4/5, as_fraction=False)
		assert (n4.exact_value == (4/5))

	def test_decimal_places_rounding(self):
		n1 = number.RealNumber(1/3, decimal_places=3)
		assert(n1.rounded_value == 0.333)

		n2 = number.RealNumber(2, decimal_places=1)
		assert(n2.rounded_value == 2)

		n3 = number.RealNumber(numerator=3, denominator=4, decimal_places=1)
		assert(n3.rounded_value == 0.8)

		n4 = number.RealNumber(9/5, as_fraction=False, decimal_places=7)
		assert (n4.rounded_value == 1.8)

		n5 = number.RealNumber(2/3, as_fraction=False, decimal_places=7)
		assert (n5.rounded_value == 0.6666667)

	def test_significant_figures_rounding(self):
		n1 = number.RealNumber(5/3)
		assert(n1.rounded_value == 1.6667)
	
		n2 = number.RealNumber(222.123, significant_figures=2)
		assert(n2.rounded_value == 220)
	
		n3 = number.RealNumber(numerator=3, denominator=4, significant_figures=1)
		assert(n3.rounded_value == 0.8)
	
		n4 = number.RealNumber(9/7, as_fraction=False)
		assert (n4.rounded_value == 1.2857)
	
		n5 = number.RealNumber(2/3, as_fraction=False, significant_figures=7)
		assert (n5.rounded_value == 0.6666667)

	def test_standard_form(self):
		n1 = number.RealNumber(1)
		assert(n1.standard_form == "1E0")

		n2 = number.RealNumber(1234567890)
		assert(n2.standard_form == "1.2346E9")

		n3 = number.RealNumber(0.00000001234)
		assert(n3.standard_form == "1.234E-8")

		n4 = number.RealNumber(123.23402, decimal_places=2)
		assert(n4.standard_form == "1.2323E2")

	def test_standard_form_setter(self):
		n1 = number.RealNumber(1)
		n1.standard_form = "5E-1"
		assert(
			n1.numerator == 1 and
			n1.denominator == 2 and
			n1.exact_value == (1/2) and
			n1.standard_form == "5E-1"
		)

		n2 = number.RealNumber(0.23, significant_figures=2)
		n2.standard_form = "1.2346E9"
		assert(
			n2.numerator == 1234600000 and
			n2.denominator == 1 and
			n2.exact_value == 1234600000 and
			n2.standard_form == "1.2E9"
		)
