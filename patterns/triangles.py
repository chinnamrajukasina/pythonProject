def print_right_triangle(n):
    print("Right-Angled Triangle:")
    for i in range(1, n + 1):
        print("*" * i)


def print_left_triangle(n):
    print("Left-Angled Triangle:")
    for i in range(1, n + 1):
        spaces = n - i
        stars = i
        print(" " * spaces + "*" * stars)


def print_equilateral_triangle(n):
    print("Equilateral Triangle:")
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)


def main():
    n = int(input("Enter the number of lines: "))
    print("Choose the type of triangle:")
    print("1. Right-Angled Triangle")
    print("2. Left-Angled Triangle")
    print("3. Equilateral Triangle")
    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        print_right_triangle(n)
    elif choice == 2:
        print_left_triangle(n)
    elif choice == 3:
        print_equilateral_triangle(n)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
