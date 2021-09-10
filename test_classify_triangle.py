from classify_triangle import classify_triangle
from itertools import permutations
import math
import unittest


class TestClassifyTriangle(unittest.TestCase):
    """
    @brief A class to test the classify_triangle function across a range of parameters.
    """

    def test_equilateral(self):
        """
        @test Tests that the function properly recognizes equilateral triangles.

        Any time all three inputs are equal, the returned string should contain "equilateral."
        """
        # Try several different positive values.
        for s in (1, 1.5, 100000.0):
            result = classify_triangle(s, s, s)
            # If it is equilateral, it can only contain that keyword, none of the others.
            self.assertTrue(result == 'equilateral',
                            'string does not match expected value of "equilateral"')

    def test_isosceles(self):
        """
        @test Tests that the function properly recognizes isosceles triangles.

        Any time two sides are the same, the returned string should contain "isosceles."
        """
        # Try several different positive values.
        for s1 in (1, 1.5, 100000.0):
            for s2 in (2.8, 7.6, 4):
                # Test that the position of the arguments doesn't matter.
                for i in range(3):
                    if i == 0:
                        result = classify_triangle(s1, s1, s2)
                    elif i == 1:
                        result = classify_triangle(s1, s2, s1)
                    else:
                        result = classify_triangle(s2, s1, s1)
                    self.assertTrue('isosceles' in result,
                                    'isosceles not present when it should be')
                    # There shouldn't be any 'equilateral' or 'scalene'. 'Right' is optional and not checked here.
                    self.assertFalse('scalene' in result,
                                     'scalene is present when it should not be')
                    self.assertFalse('equilateral' in result,
                                     'equilateral is present when it should not be')
                    self.assertFalse('invalid' in result,
                                     'invalid is present when it should not be')

    def test_scalene(self):
        """
        @test Tests that the function properly recognizes scalene triangles.

        Any time the three sides are different lengths, the returned string should contain "scalene."
        """
        # Just pick some different values.
        inputs = []
        inputs.append((1.0, 2.0, 3.0))
        inputs.append((3.0, 4.0, 5.0))
        inputs.append((1000, 2000, 3000))
        for input in inputs:
            result = classify_triangle(input[0], input[1], input[2])
            self.assertTrue('scalene' in result,
                            'scalene not present when it should be')
            # It should not have "isosceles" or "equilateral." "right" is irrelevant.
            self.assertFalse('equilateral' in result,
                             'equilateral present when it should not be')
            self.assertFalse('isosceles' in result,
                             'isosceles present when it should not be')
            self.assertFalse('invalid' in result,
                             'invalid present when it should not be')

    def test_right(self):
        """
        @test Tests that the function properly recognizes right triangles.

        Any time the three sides match the required for right triangles, the returned string should contain "right."
        Any other values are also permitted in this string.
        """
        # Pick two numbers and calculate the third.
        s1 = 3.0
        s2 = 4.0
        s3 = math.sqrt(s1 ** 2 + s2 ** 2)
        # The order of arguments shouldn't matter. I got the example of using permutations from:
        # https://www.geeksforgeeks.org/permutation-and-combination-in-python/
        unique_orders = permutations([s1, s2, s3])
        for single_order in unique_orders:
            result = classify_triangle(
                single_order[0], single_order[1], single_order[2])
            self.assertTrue('right' in result)
            self.assertFalse('invalid' in result)

    def test_invalid(self):
        """
        @test Tests that the function rejects invalid cases.

        Any time invalid arguments are supplied, return "invalid." This includes:
        * Any side is a nonpositive number
        * Any side is not a number
        """
        # All of these should only have the string "invalid" with nothing else.
        result = classify_triangle(0, 0, 0.0)
        self.assertTrue(result == 'invalid')
        # This also makes sure that "right" doesn't get prepended on.
        result = classify_triangle(-3.0, 4.0, 5.0)
        self.assertTrue(result == 'invalid')
        result = classify_triangle('3.0', 4.0, 5.0)  # type: ignore
        self.assertTrue(result == 'invalid')
