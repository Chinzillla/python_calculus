import sympy as sp

def find_instantaneous_rate_of_change_at_point_of_time(tangent_line_string: str, point: float) -> None:
    '''
    @Function: Extract the instantaneous rate of change (slope) from the tangent line
    @arg: tangent_line_string - String representation of the tangent line equation
    @return: Float - The slope of the tangent line (instantaneous rate of change)
    '''
    x = sp.Symbol('x')
    tangent_line = sp.sympify(tangent_line_string)
    result = tangent_line.subs(x, point)
    print(float(result))