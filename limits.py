import sympy as sp

# Define variable
x = sp.symbols('x')

# Example 1: Limit as x approaches 0 of sin(x)/x
expr1 = sp.sin(x) / x
limit1 = sp.limit(expr1, x, 0)

# Example 2: Limit as x approaches infinity of (1 + 1/x)^x
expr2 = (1 + 1/x)**x
limit2 = sp.limit(expr2, x, sp.oo)

# Example 3: Limit as x approaches 1 of (x^2 - 1)/(x - 1)
expr3 = (x**2 - 1) / (x - 1)
limit3 = sp.limit(expr3, x, 1)

# Example 4: Limit as x approaches 0 from the right of 1/x
expr4 = 1 / x
limit4 = sp.limit(expr4, x, 0, dir='+')

# Explanation of the process
explanations = {
    "Example 1": "The limit of sin(x)/x as x approaches 0 is a standard result in calculus, and it evaluates to 1. This is often derived using the squeeze theorem.",
    "Example 2": "The limit of (1 + 1/x)^x as x approaches infinity is the definition of Euler's number e, and it evaluates to e.",
    "Example 3": "The limit of (x^2 - 1)/(x - 1) as x approaches 1 involves factoring the numerator to get (x - 1)(x + 1)/(x - 1). After canceling the (x - 1) terms, the limit is 2.",
    "Example 4": "The limit of 1/x as x approaches 0 from the right goes to positive infinity because the values of 1/x increase without bound as x gets closer to 0 from the positive side."
}

# Print results
results = {
    "Example 1: Limit of sin(x)/x as x -> 0": limit1,
    "Example 2: Limit of (1 + 1/x)^x as x -> infinity": limit2,
    "Example 3: Limit of (x^2 - 1)/(x - 1) as x -> 1": limit3,
    "Example 4: Limit of 1/x as x -> 0+": limit4
}

for key, value in results.items():
    print(f"{key}: {value}\n")

print("\nExplanations:")
for key, explanation in explanations.items():
    print(f"{key}: {explanation}\n")