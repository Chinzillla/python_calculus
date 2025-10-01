import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def visualize_polynomial_with_tangent(polynomial_str: str, tangent_line_str: str, point: float) -> None:
    '''
    @Function: Visualize the polynomial curve and its tangent line together
    @arg: polynomial_str - String representation of the polynomial equation
    @arg: tangent_line_str - String representation of the tangent line equation
    @arg: point - The x-coordinate where the tangent line touches the curve
    @return: None - Displays the plot
    '''
    x = sp.Symbol('x')
    polynomial = sp.sympify(polynomial_str)
    tangent_line = sp.sympify(tangent_line_str)
    
    poly_func = sp.lambdify(x, polynomial, 'numpy')
    tangent_func = sp.lambdify(x, tangent_line, 'numpy')
    
    x_range = np.linspace(point - 10, point + 10, 1000)
    y_poly = poly_func(x_range)
    y_tangent = tangent_func(x_range)
    
    y_point = poly_func(point)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x_range, y_poly, 'b-', linewidth=2, label='Polynomial Curve')
    plt.plot(x_range, y_tangent, 'r--', linewidth=2, label='Tangent Line')
    plt.plot(point, y_point, 'go', markersize=10, label=f'Point of Tangency ({point}, {y_point:.2f})')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Curve with Tangent Line')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    slope = sp.diff(tangent_line, x)
    text_str = f'Polynomial: {polynomial_str}\n'
    text_str += f'Tangent Line: {tangent_line_str}\n'
    text_str += f'Instantaneous Rate at x={point}: {float(slope):.2f}'
    
    plt.text(0.02, 0.98, text_str, 
             transform=plt.gca().transAxes, 
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8),
             fontsize=10)
    
    plt.show()