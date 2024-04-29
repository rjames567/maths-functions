# def parse_expression(expression_str):
# 	expression_str = expression_str.replace("x", "*x")
# 	if expression_str[0] == "*":
# 		expression_str = expression_str[1:]
# 	print(expression_str)
# 	return lambda x: eval(expression_str.replace('x', str(x)))

# def find_solution(expression_str, x_range, step=0.1, tol=1e-6, max_iter=100):
# 	# expression = parse_expression(expression_str)
# 	# for x0 in [x_range[0] + step * i for i in range(int((x_range[1] - x_range[0]) / step))]:
# 	# 	iteration = 0
# 	# 	while iteration < max_iter:
# 	# 		f_val = expression(x0)
# 	# 		if abs(f_val) < tol:
# 	# 			return x0
# 	# 		f_prime_val = (expression(x0 + tol) - expression(x0 - tol)) / (2 * tol)
# 	# 		if abs(f_prime_val) < tol:
# 	# 			break
# 	# 		x0 = x0 - f_val / f_prime_val
# 	# 		iteration += 1
# 	# raise ValueError("Failed to find a solution within the given range.")
# 	expression = parse_expression(expression_str)
# 	for x0 in [x_range[0] + step * i for i in range(int((x_range[1] - x_range[0]) / step))]:
# 		iteration = 0
# 		while iteration < max_iter:
# 			f_val = expression(x0)
# 			if abs(f_val) < tol:
# 				return x0
# 			f_prime_val = (expression(x0 + tol) - expression(x0 - tol)) / (2 * tol)
# 			if abs(f_prime_val) < tol:
# 				break  # Avoid division by zero
# 			x0 = x0 - f_val / f_prime_val
# 			iteration += 1
# 		# If the loop completes without convergence, move to the next point
# 	raise ValueError("No solution found within the given range.")

# if __name__ == "__main__":
# 	expression_str = input("Enter the expression (e.g x^2 + 2x + 1): ").replace("^", "**")
# 	solution = find_solution(expression_str, x_range=(-10, 10))
# 	print("Approximate solution:", solution)
def parse_expression(expression_str):
	"""
	Parses the expression string and returns a lambda function representing the expression.

	Parameters:
	expression_str (str): The expression string to be parsed.

	Returns:
	function: Lambda function representing the parsed expression.
	"""
	return lambda x: eval(expression_str.replace('x', str(x)))

def find_solution(expression, x_range, step=0.1, tol=1e-6, max_iter=100):
	"""
	Finds the solution to the equation by finding the gradient at a range of points.

	Parameters:
	expression_str (str): The expression string to be parsed.
	x_range (tuple): Range of x values to search for the solution.
	step (float): Step size for searching.
	tol (float): Tolerance level for convergence.
	max_iter (int): Maximum number of iterations for each point.

	Returns:
	float: Approximation of the root.
	"""
	for x0 in [x_range[0] + step * i for i in range(int((x_range[1] - x_range[0]) / step))]:
		x_initial = x0
		iteration = 0
		found_solution = False
		while iteration < max_iter:
			f_val = expression(x0)
			if abs(f_val) < tol:
				found_solution = True
				break
			f_prime_val = (expression(x0 + tol) - expression(x0 - tol)) / (2 * tol)
			if abs(f_prime_val) < tol:
				break  # Avoid division by zero
			x0 = x0 - f_val / f_prime_val
			iteration += 1
		if found_solution:
			return x0
	raise ValueError("No solution found within the given range.")

import math
if __name__ == "__main__":
	expression_str = "x**2 + 2*x + 5"
	try:
		# parsed = parse_expression(expression_str)
		parsed = lambda x: ((x ** 3) * math.log(x ** 2)) + (x ** -2) - (4 * x)
		solution = find_solution(parsed, x_range=(-10, 10))
		print("Approximate solution:", solution)
	except ValueError as e:
		print(e)

