import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def visualize_tangent_line(tangent_line_string: str) -> None:
    '''
    @Function: Visualize only the tangent line
    @arg: tangent_line_string - String representation of the tangent line equation
    @return: None - Displays the plot
    '''
    x = sp.Symbol('x')
    tangent_line = sp.sympify(tangent_line_string)
    tangent_func = sp.lambdify(x, tangent_line, 'numpy')
    
    x_range = np.linspace(0, 20, 100)
    y_tangent = tangent_func(x_range)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_tangent, 'r-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Tangent Line: {tangent_line_string}')
    plt.grid(True, alpha=0.3)
    
    slope = sp.diff(tangent_line, x)
    plt.text(0.02, 0.98, f'Slope (Instantaneous Rate): {float(slope):.2f}', 
             transform=plt.gca().transAxes, 
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))
    
    plt.show()