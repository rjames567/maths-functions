import number

# n = number.RealNumber(numerator=1, denominator=2)
# n._disp_vars()

# print()

# n = number.RealNumber(5)
# n._disp_vars()

# print()

n = number.RealNumber(1/3)
n._disp_vars()
n.numerator = 2
n._disp_vars()

n.denominator = 10
n._disp_vars()

n.denominator = "2.5"

# n = number.RealNumber(1/3, as_fraction=False)
# n._disp_vars()
