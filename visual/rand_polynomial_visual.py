import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def visualize_polynomial(polynomial_str: str) -> None:
    '''
    @Function: Visualize only the polynomial curve
    @arg: polynomial_str - String representation of the polynomial equation
    @return: None - Displays the plot
    '''
    # Convert string to sympy expression
    x = sp.Symbol('x')
    polynomial = sp.sympify(polynomial_str)
    
    # Convert to numpy function
    poly_func = sp.lambdify(x, polynomial, 'numpy')
    
    # Create x range for plotting
    x_range = np.linspace(0, 20, 1000)
    y_values = poly_func(x_range)
    
    # Get polynomial degree for title
    degree = sp.degree(polynomial, x)
    
    # Plot the curve
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_values, 'b-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Polynomial Curve (Degree {degree}): {polynomial_str}')
    plt.grid(True, alpha=0.3)
    plt.show()