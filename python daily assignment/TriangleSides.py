def is_right_triangle(side1, side2, side3):
    # Sort the sides in ascending order
    sides = sorted([side1, side2, side3])

    # Check the Pythagorean Theorem
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        return True
    else:
        return False


# Input lengths of the sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Check if it's a right triangle
if is_right_triangle(side1, side2, side3):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")
