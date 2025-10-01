import sympy as sp

def parse_polynomial(polynomial_string: str):
    '''
    @Function: Convert a polynomial string to a SymPy expression
    @arg: polynomial_string - String representation of polynomial (e.g., "3*x**2 + 2*x - 5")
    @return: SymPy expression - The parsed polynomial
    '''
    # Convert string to sympy expression
    x = sp.Symbol('x')
    polynomial = sp.sympify(polynomial_string)
    print(polynomial)
    return polynomial
