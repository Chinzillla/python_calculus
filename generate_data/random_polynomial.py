import random
# import matplotlib.pyplot as plt

def generate_random_curve() -> str:
    '''
    @Function: Generate a random curve to find the instantaneous rate of change of
    @arg: None
    @return: String: The curves equation
    '''
    degree = random.randint(2, 5)
    coefficients = [random.uniform(-5, 5) for _ in range(degree + 1)]
    print(coefficients)
    
    '''
    @Display the function generated above in a graph

    t = np.linspace(0, 10, 1000)
    
    # Calculate position using polynomial
    position = np.polyval(coefficients, t)
    
    # Plot the curve
    plt.figure(figsize=(10, 6))
    plt.plot(t, position, 'b-', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.title(f'Random Polynomial Curve (Degree {degree})')
    plt.grid(True)
    plt.show()
    '''
    
    polynomial_function = ''
    
    terms = []
    for i, coefficient in enumerate(coefficients):
        power = degree - i

        coefficient_string = f"{coefficient:.2f}"
        if power == 0:
            terms.append(coefficient_string)
        elif power == 1:
            terms.append(f"{coefficient_string}*x")
        else:
            terms.append(f"{coefficient_string}*x**{power}")
    
    polynomial_function = ' + '.join(terms)
    # Replace "+ -" with "- " for cleaner formatting
    polynomial_function = polynomial_function.replace('+ -', '- ')

    print(polynomial_function)

    return polynomial_function