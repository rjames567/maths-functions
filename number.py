import fractions

superscript = {
	0: "⁰",
	1: "¹",
	2: "²",
	3: "³",
	4: "⁴",
	5: "⁵",
	6: "⁶",
	7: "⁷",
	8: "⁸",
	9: "⁹"
}

class RealNumber:
	def __init__(self, value=None, fraction_threshold=1, as_fraction=True, **kwargs):
		"""
		Parameters:
			value (float)				->		Value of the number.
			numerator (int)				->		Numerator of the fraction.
			denominator (int)			-> 		Denominator of the fraction
			fraction_threshold (int)	->		The number of decimal places before the number is represented as a fraction. 0 means never represent as a fraction (Default: 1)
			as_fraction (bool)			->		Whether the value should be treated as the true value, or as a fraction. True value will be faster, but may be less accurate. (Default: True)
			decimal_places (int)		->		The number of decimal places to round to. Only applies if as_fraction is false. (Default: None)
			significant_figures (int)	->		The number of significant figures to round to. Only applies if as_fraction is false. (Default: 5)
		"""

		self._as_fraction = as_fraction
		
		if value is not None:
			self._value = value
			if type(self._value) is int or not self._as_fraction:
				self._numerator = self._value
				self._denominator = 1
			else:
				self._simplify_fraction()
				
		else:
			self._numerator = kwargs["numerator"]
			self._denominator = kwargs["denominator"]
			self._value = self._numerator / self._denominator

		self._fraction_threshold = fraction_threshold

		self._decimal_places = kwargs.get("decimal_places", None)
		self._significant_figures = kwargs.get("significant_figures", None)

		if self._significant_figures is None and self._decimal_places is None:
			self._significant_figures = 5
		elif self._significant_figures >= self._decimal_places:
			self._decimal_places = None
		else:
			self._significant_figures = None

	def _simplify_fraction(self):
		if self._as_fraction:
			self._numerator, self._denominator = tuple(str(fractions.Fraction(self._value).limit_denominator(max_denominator=100000)).split("/"))

	def _disp_vars(self):
		print("Variables")
		print(f"\t_value: {self._value}")
		print(f"\t_numerator: {self._numerator}")
		print(f"\t_denominator: {self._denominator}")
		print(f"\t_fraction_threshold: {self._fraction_threshold}")
		print(f"\t_as_fraction: {self._as_fraction}")
		print(f"\t_decimal_places: {self._decimal_places}")
		print(f"\t_significant_figures: {self._significant_figures}")

		print("@property")
		print(f"\tdenominator: {self.denominator}")
		print(f"\tnumerator: {self.numerator}")
		print()

	@property
	def denominator(self):
		if self._as_fraction:
			return self._denominator
		else:
			return None

	@property
	def numerator(self):
		if self._as_fraction:
			return self._numerator
		else:
			return None