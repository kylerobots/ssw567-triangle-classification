"""
A module that helps classify types of triangles.
"""
import argparse
import sys
from typing import List, Tuple


def classify_triangle(side1: float, side2: float, side3: float) -> str:
    """
    @brief Classify the type of a triangle based on its sides.

    Returns a string with the type of triangle according to the following definitions:
    * "equilateral": All three sides are the same length
    * "isosceles": Two sides are the same length
    * "scalene": All three sides are different lengths
    * "right": The sides follow the Pythagorean theorem (this can be in
    addition to the previous three)
    * "invalid": The provided arguments do not represent a valid triangle

    @example
    * classify_triangle(1, 1, 1) returns "equilateral"
    * classify_triangle(3, 4, 5) returns "right scalene"
    * classify_triangle(0, 0, 0) returns "invalid"

    @param side1 The first edge of the triangle (order does not matter)
    @param side2 The second edge of the triangle (order does not matter)
    @param side3 The last edge of the triangle (order does not matter)
    @return A string containing the classification of the triangle
    """
    # First, verify that all arguments are numbers greater than 0. This can't
    # be a triangle otherwise.
    # This is also where any non-numeric types will throw errors. So watch for
    # that and return "invalid" if it occurs.
    try:
        if not (side1 > 0.0 and side2 > 0.0 and side3 > 0.0):
            return 'invalid'
    except TypeError:
        return 'invalid'
    # Verify the triangle inequality holds for all combinations of sides. Use
    # the strict case to avoid degenerate
    # triangles.
    ineq12 = side1 + side2 > side3
    ineq13 = side1 + side3 > side2
    ineq23 = side2 + side3 > side1
    if not (ineq12 and ineq13 and ineq23):
        return 'invalid'
    # Then, see if it is an equilateral triangle, which can't also be right.
    if side1 == side2 and side1 == side3:
        return 'equilateral'
    # Next, isosceles and scalene triangles can be right, so check that. Watch for floating point.
    # Since the order of the sides doesn't matter, check all possible combinations
    right12 = side1**2 + side2**2 == side3**2
    right13 = side1**2 + side3**2 == side2**2
    right23 = side2**2 + side3**2 == side1**2
    if right12 or right13 or right23:
        result = 'right '
    else:
        result = ''
    # Now see if it is an isosceles triangle
    iso12 = side1 == side2
    iso13 = side1 == side3
    iso23 = side2 == side3
    if iso12 or iso13 or iso23:
        result += 'isosceles'
    else:
        # If it isn't any of the above, it has to be scalene
        result += 'scalene'
    return result


def parse_arguments(arguments: List[str]) -> Tuple[float, float, float]:
    """
    @brief Parse the command line arguments into the triangle sides.
    @param arguments The command line input from the user.
    @return A tuple containing the three sides of the triangle.
    @raise argparse.ArgumentError raised if the arguments are not convertable to floats.
    """
    # Use of argparse comes from its documentation: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(
        description='Classify a triangle based on side length.')
    parser.add_argument('side_1', metavar='side_1',
                        type=float, help='The first side of the triangle.')
    parser.add_argument('side_2', metavar='side_2',
                        type=float, help='The second side of the triangle.')
    parser.add_argument('side_3', metavar='side_3',
                        type=float, help='The third side of the triangle.')
    args = parser.parse_args(arguments)
    result = (args.side_1, args.side_2, args.side_3)
    return result


if __name__ == '__main__':
    (side_1, side_2, side_3) = parse_arguments(sys.argv[1:])
    TRIANGLE_TYPE = classify_triangle(side_1, side_2, side_3)
    print(f'This is a {TRIANGLE_TYPE} triangle.')
