import sympy as sp

# Define variables
x = sp.symbols('x')

# a. Derivative of a constant multiple of a function
c = sp.symbols('c')  # constant
f = sp.Function('f')(x)
expr_a = c * f
result_a = sp.diff(expr_a, x)

# b. Derivative of the sum (or difference) of two functions
g = sp.Function('g')(x)
expr_b = f + g  # Sum of two functions
result_b = sp.diff(expr_b, x)

# c. Derivative of the product of two functions
expr_c = f * g  # Product of two functions
result_c = sp.diff(expr_c, x)

# d. Derivative of the quotient of two functions
expr_d = f / g  # Quotient of two functions
result_d = sp.diff(expr_d, x)

# Print results
results = {
    "a. Derivative of constant multiple of a function": result_a,
    "b. Derivative of sum or difference of two functions": result_b,
    "c. Derivative of product of two functions": result_c,
    "d. Derivative of quotient of two functions": result_d
}

for key, value in results.items():
    print(f"{key}: {value}\n")
