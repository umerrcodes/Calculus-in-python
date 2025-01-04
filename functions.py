import sympy as sp

# Define a function for differentiation
def differentiate(expr, var):
    return sp.diff(expr, var)

# Define a function for integration
def integrate(expr, var):
    return sp.integrate(expr, var)

# Define a function for finding limits
def limit(expr, var, point):
    return sp.limit(expr, var, point)

# Define a function for finding critical points
def critical_points(expr, var):
    derivative = sp.diff(expr, var)
    return sp.solve(derivative, var)

# Example usage
if __name__ == "__main__":
    x = sp.symbols('x')
    expr = x**2 + 3*x + 2

    print("Function:", expr)
    print("Derivative:", differentiate(expr, x))
    print("Integral:", integrate(expr, x))
    print("Limit as x approaches 1:", limit(expr, x, 1))
    print("Critical Points:", critical_points(expr, x))