import math

# The triangle module has functions that perform
# calculations related to triangles.

# This area function accepts a triangle's base and
# height as arguments and returns the triangle's area.
def area_with_base_and_height(base, height):
    return 0.5 * base * height

# This area function accepts a triangle's sides
# as arguments and returns the triangle's area using the herons
# herons formula.
def area_with_herons_formula(a, b, c):
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# The perimeter function accepts three sides as arguments
# and returns the triangle's perimeter.
def perimeter(a, b, c):
    return a + b + c 