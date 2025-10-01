from generate_data.random_polynomial import generate_random_curve
from tools.parse_polynomial import parse_polynomial
from tools.find_tangent_line import find_tangent_line
from tools.instantaneous_rate_of_change import find_instantaneous_rate_of_change_at_point_of_time

def main():
    polynomial_string = generate_random_curve()
    polynomial = parse_polynomial(polynomial_string)
    tangent_line = find_tangent_line(polynomial, 10)
    find_instantaneous_rate_of_change_at_point_of_time(tangent_line, 10)

if __name__ == "__main__":
    main()