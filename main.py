from classify_triangle import classify_triangle
import argparse

if __name__ == '__main__':
    # Use of argparse comes from its documentation: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(
        description='Classify a triangle based on side length.')
    parser.add_argument('side_1', metavar='side_1',
                        type=float, help='The first side of the triangle.')
    parser.add_argument('side_2', metavar='side_2',
                        type=float, help='The second side of the triangle.')
    parser.add_argument('side_3', metavar='side_3',
                        type=float, help='The third side of the triangle.')
    args = parser.parse_args()
    result = classify_triangle(args.side_1, args.side_2, args.side_3)
    print('This is a {0:s} triangle.'.format(result))
