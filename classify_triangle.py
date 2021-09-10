def classify_triangle(s1: float, s2: float, s3: float) -> str:
    """
    @brief Classify the type of a triangle based on its sides.

    Returns a string with the type of triangle according to the following definitions:
    * "equilateral": All three sides are the same length
    * "isosceles": Two sides are the same length
    * "scalene": All three sides are different lengths
    * "right": The sides follow the Pythagorean theorem (this can be in addition to the previous three)
    * "invalid": The provided arguments do not represent a valid triangle

    @example
    * classify_triangle(1, 1, 1) returns "equilateral"
    * classify_triangle(3, 4, 5) returns "right scalene"
    * classify_triangle(0, 0, 0) returns "invalid"

    @param s1 The first edge of the triangle (order does not matter)
    @param s2 The second edge of the triangle (order does not matter)
    @param s3 The last edge of the triangle (order does not matter)
    @return A string containing the classification of the triangle
    """
    return ''
