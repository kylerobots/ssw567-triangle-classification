"""
Module to test the classify_triangle module.
"""

import argparse
from itertools import permutations
import unittest
from classify_triangle import classify_triangle, parse_arguments


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
        for side in (1, 1.5, 100000.0):
            result = classify_triangle(side, side, side)
            # If it is equilateral, it can only contain that keyword, none of the others.
            self.assertTrue(result == 'equilateral',
                            'string does not match expected value of "equilateral"')

    def test_isosceles(self):
        """
        @test Tests that the function properly recognizes isosceles triangles.

        Any time two sides are the same, the returned string should contain "isosceles."
        """
        # Try several different positive values.
        for leg in (2.8, 7.6, 1000.0):
            for base in (1, 1.5, 1.25):
                # Test that the position of the arguments doesn't matter.
                for i in range(3):
                    if i == 0:
                        result = classify_triangle(leg, leg, base)
                    elif i == 1:
                        result = classify_triangle(leg, base, leg)
                    else:
                        result = classify_triangle(base, leg, leg)
                    self.assertTrue('isosceles' in result,
                                    'isosceles not present when it should be')
                    # There shouldn't be any 'equilateral' or 'scalene'.
                    # 'Right' is optional and not checked here.
                    self.assertFalse('scalene' in result,
                                     'scalene is present when it should not be')
                    self.assertFalse('equilateral' in result,
                                     'equilateral is present when it should not be')
                    self.assertFalse('invalid' in result,
                                     'invalid is present when it should not be')

    def test_scalene(self):
        """
        @test Tests that the function properly recognizes scalene triangles.

        Any time the three sides are different lengths, the returned string
        should contain "scalene."
        """
        # Just pick some different values.
        inputs = []
        inputs.append((1.0, 2.0, 2.5))
        inputs.append((3.0, 4.0, 5.0))
        inputs.append((1000, 2000, 2500))
        for single_input in inputs:
            result = classify_triangle(
                single_input[0], single_input[1], single_input[2])
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

        Any time the three sides match the required for right triangles, the
        returned string should contain "right."
        Any other values are also permitted in this string.
        """
        # Pick known Pythagorean numbers.
        side1 = 3.0
        side2 = 4.0
        side3 = 5.0
        # The order of arguments shouldn't matter. I got the example of using permutations from:
        # https://www.geeksforgeeks.org/permutation-and-combination-in-python/
        unique_orders = permutations([side1, side2, side3])
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
        * Triangle inequality is violated
        """
        inputs = []
        inputs.append((0, 0, 0.0))
        inputs.append(('3.0', 4.0, 5.0))
        result = classify_triangle('3.0', 4.0, 5.0)  # type: ignore
        # This also makes sure that "right" doesn't get prepended on.
        inputs.append((-3.0, 4.0, 5.0))
        # The sum of any two of the sides of a triangle must be greater than the third:
        # https://en.wikipedia.org/wiki/Triangle#Condition_on_the_sides
        inputs.append((1.0, 2.0, 3.0))
        inputs.append((0.5, 0.5, 2.0))
        for single_input in inputs:
            result = classify_triangle(
                single_input[0], single_input[1], single_input[2])
            # All of these should only have the string "invalid" with nothing else.
            self.assertTrue(
                result == 'invalid', f'result should be invalid, but it is {result}')

    def test_arg_parse(self):
        """
        @test Tests that the command line argument parser works as intended.
        """
        # Floats and ints should parse fine
        expected_list = (1.0, 2.0, 3.0)
        results = parse_arguments(['1.0', '2.0', '3.0'])
        self.assertTupleEqual(results, expected_list,
                              'Float inputs not handled correctly')
        results = parse_arguments(['1', '2', '3'])
        self.assertTupleEqual(results, expected_list,
                              'Int inputs not handled correctly')
        # Other datatypes should not. The tests will stop after the first,
        # because of SystemExit, so do this three seperate times.
        with self.assertRaises((argparse.ArgumentError, ValueError, SystemExit)):
            parse_arguments(['blah', '2.0', '3.0'])
        with self.assertRaises((argparse.ArgumentError, ValueError, SystemExit)):
            parse_arguments(['1.0', '2.0', 'blah'])
        with self.assertRaises((argparse.ArgumentError, ValueError, SystemExit)):
            parse_arguments(['1.0', 'blah', '3.0'])


if __name__ == '__main__':
    unittest.main()
