# Import the specific function from the module
from math_operations import add


def main():
    # Use the imported add function
    result = add(5, 3)

    # Display the result
    print(f"Result of addition: {result}")


if __name__ == "__main__":
    main()
