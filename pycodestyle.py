#!/usr/bin/python3
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    area = length * width
    return area


def main():
    # Input
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Calculate area
    area = calculate_area(length, width)

    # Output
    print("The area of the rectangle is:", area)


if __name__ == "__main__":
    main()

