# ssw567-triangle-classification #
A homework assignment to test a function that classifies triangles based on their side lengths.

This creates a function, *classify_triangle* that determines the type of a triangle based on its side lengths. It
returns a string containing the type. There are several types that can be returned:

| Type | Description |
| --- | --- |
| Equilateral | All three sides are the same length (exclusive with Isosceles and Scalene) |
| Isosceles | Two sides are the same length (exclusive with Isosceles and Scalene) |
| Scalene | All three sides are different lengths (exclusive with Isosceles and Scalene) |
| Right | Can modify Isosceles or Scalene if the sides meet the Pythagorean Theorem |
| Invalid | Returned if the sides do not form a valid triangle |

## Calling the Function ##
The classifier has the following command line arguments:
```
python classify_triangle.py side_1 side_2 side_3
```
The order of the sides do not matter. The result is printed to the command line and looks similar to this:
```
This is a right scalene triangle.
```
If the sides do not form a valid triangle, it will return the following:
```
This is a invalid triangle.
```

You can also call the function directly in your own program. See the docstring for the API.

## Running Unit Tests ##
This repository uses unittest for testing. To run the tests, use the following command:
```
python -m unittest -v
```