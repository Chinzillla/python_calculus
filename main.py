from generate_data.random_polynomial import generate_random_curve
from tools.parse_polynomial import parse_polynomial
from tools.find_tangent_line import find_tangent_line
from tools.instantaneous_rate_of_change import find_instantaneous_rate_of_change_at_point_of_time
from visual.rand_polynomial_visual import visualize_polynomial
from visual.tangent_line_visual import visualize_tangent_line
from visual.rand_polynomial_tangent_line_visual import visualize_polynomial_with_tangent

def main():
    polynomial_string = generate_random_curve()
    polynomial = parse_polynomial(polynomial_string)

    point = 10

    tangent_line_string = find_tangent_line(polynomial, point)
    find_instantaneous_rate_of_change_at_point_of_time(tangent_line_string, point)
    visualize_polynomial(polynomial_string)
    visualize_tangent_line(tangent_line_string)
    visualize_polynomial_with_tangent(polynomial_string, tangent_line_string, point)

if __name__ == "__main__":
    main()