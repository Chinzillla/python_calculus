import sympy as sp

def find_tangent_line(polynomial, point: float) -> str:
    '''
    @Function: Find the tangent line equation at a specific point on a polynomial curve
    @arg: polynomial_string - String representation of polynomial (e.g., "3*x^2 + 2*x - 5")
    point - The x-coordinate where the tangent line touches the curve
    @return: String - The tangent line equation
    '''
    # Define the variable
    x = sp.Symbol('x')

    derivative = sp.diff(polynomial, x)
    slope = derivative.subs(x, point)
    y_at_point = polynomial.subs(x, point)
    
    tangent_line = slope * (x - point) + y_at_point
    
    tangent_line_str = str(tangent_line)
    print(tangent_line_str)
    return tangent_line_str