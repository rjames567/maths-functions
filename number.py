import fractions
import math

superscript = {
	"0": "⁰",
	"1": "¹",
	"2": "²",
	"3": "³",
	"4": "⁴",
	"5": "⁵",
	"6": "⁶",
	"7": "⁷",
	"8": "⁸",
	"9": "⁹",
	"-": "⁻"
}

class RealNumber:
	def __init__(self, value=None, fraction_threshold=1, as_fraction=True, standard_form_threshold=(1E8, 1E-8), as_standard_form=False, **kwargs):
		"""
		Parameters:
			value (float)						->		Value of the number.
			numerator (int)						->		Numerator of the fraction.
			denominator (int)					-> 		Denominator of the fraction
			fraction_threshold (int)			->		The number of decimal places before the number is represented as a fraction. 0 means always represent as a fraction (Default: 1)
			as_fraction (bool)					->		Whether the value should be treated as the true value, or as a fraction. True value will be faster, but may be less accurate. (Default: True)
			decimal_places (int)				->		The number of decimal places to round to. Only applies if as_fraction is false. (Default: None)
			significant_figures (int)			->		The number of significant figures to round to. Only applies if as_fraction is false. (Default: 5)
			standard_form_threshold	(tuple)		->		The point at which the number will be represented in standard form when given as a string. Gives both the upper and lower points. Se. (Default: 1E8, 1E-8)
			as_standard_form (bool)				->		Flag that specifies whether the value should be shown in standard form. If set to False, it will be in standard form if it is outside the range specified by standard_form_threshold. If set to True, it will always be in standard form, when given as a string (Default: False)
		"""

		self._as_fraction = as_fraction
		
		if value is not None:
			self._value = float(value)
			self._numerator = self._value
			self._denominator = 1
			if type(self._value) is not int and self._as_fraction:
				self._simplify_fraction()
				
		else:
			self._numerator = kwargs["numerator"]
			self._denominator = kwargs["denominator"]
			self._value = self._numerator / self._denominator

		self._fraction_threshold = fraction_threshold
		self._standard_form_threshold = (min(standard_form_threshold), max(standard_form_threshold))
		self._as_standard_form = as_standard_form
		

		self._decimal_places = kwargs.get("decimal_places", None)
		self._significant_figures = kwargs.get("significant_figures", None)

		if self._significant_figures is None and self._decimal_places is None:
			self._significant_figures = 5
		elif self._significant_figures is not None and self._decimal_places is not None:
			if self._significant_figures >= self._decimal_places:
				self._decimal_places = None
			else:
				self._significant_figures = None

	def _simplify_fraction(self, recalculate_value=True):
		if self._as_fraction:
			if recalculate_value:
				self._value = self._numerator / self._denominator
			temp = tuple(str(fractions.Fraction(self._value).limit_denominator(max_denominator=100000)).split("/"))
			self._numerator = int(temp[0])
			self._denominator = int(temp[1]) if len(temp) > 1 else 1

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
		print(f"\texact_value: {self.exact_value}")
		print(f"\trounded_value: {self.rounded_value}")
		print(f"\tstandard_form: {self.rounded_value}")
		print()

	def _round(self, decimal_places=None):
		if decimal_places is None:
			if self._significant_figures is not None:
				# https://stackoverflow.com/a/3413529
				return round(self._value, self._significant_figures - int(math.floor(math.log10(abs(self._value)))) - 1)
			decimal_places = self._decimal_places
		return round(self._value, decimal_places)

	@property
	def decimal_part(self):
		return self._value - int(self._value)

	@property
	def denominator(self):
		if self._as_fraction:
			return self._denominator
		else:
			return None

	@denominator.setter
	def denominator(self, value):
		if self._as_fraction:
			if type(value) == int:
				self._denominator = value
				self._simplify_fraction()
				self._value = self._numerator / self._denominator
			else:
				dtype = repr(type(value)).split("'")[1]
				raise Exception(f"Cannot assign denominator to '{dtype}'. Numerator must be an integer")
		else:
			raise Exception("Cannot assign denominator to a RealNumber that is not a fraction.")
	
	@property
	def numerator(self):
		if self._as_fraction:
			return self._numerator
		else:
			return None

	@numerator.setter
	def numerator(self, value):
		if self._as_fraction:
			if type(value) == int:
				self._numerator = value
				self._simplify_fraction()
				self._value = self._numerator / self._denominator
			else:
				dtype = repr(type(value)).split("'")[1]
				raise Exception(f"Cannot assign numerator to '{dtype}'. Numerator must be an integer")
		else:
			raise Exception("Cannot assign numerator to a RealNumber that is not a fraction.")

	@property
	def exact_value(self):
		return self._value

	@exact_value.setter
	def exact_value(self, value):
		self._value = float(value)

	@property
	def rounded_value(self):
		return self._round()

	@rounded_value.setter
	def rounded_value(self, value):
		self._value = value

	@property
	def standard_form(self):
		string = str(self.rounded_value)
		if "e" not in string:
			string = '{:.10000e}'.format(self.rounded_value)  # Arbitrarily large number for precision chosen as it cannot accurately represent this high, so shouldnt be rounded this much.
		components = [float(i) for i in string.split("e")]
		if int(components[0]) == components[0]:
			components[0] = int(components[0])
		if int(components[1]) == components[1]:
			components[1] = int(components[1])

		return str(components[0]) + "E" + str(components[1])

	@standard_form.setter
	def standard_form(self, value):
		self._value = float(value)
		self._simplify_fraction(recalculate_value=False)

	# Magic Method
	# https://www.geeksforgeeks.org/dunder-magic-methods-python/
	def __round__(self, places=None):
		# If number of places is not specified, rounds to the accuracy as given in the parameters, otherwise number of decimal places given.
		return self._round(places)

	def __abs__(self):
		return abs(self._value)

	def __bool__(self):
		return bool(self._value)

	def __str__(self):
		if self._as_standard_form:
			return self.standard_form
		else:
			if self._as_fraction:
				if len(str(self.decimal_part)[2:]) > self._fraction_threshold:
					return f"{self._numerator}/{self._denominator}"
				else:
					return str(self._value)
		return str(self.rounded_value)

	def __int__(self):
		return int(self._value)

	def __float__(self):
		return float(self._value)