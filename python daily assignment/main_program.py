# Import the Fibonacci module
import fibonacci_module


def main():
    # Use the generate_fibonacci function from the imported module
    n = 10  # Change this value to the desired length of the Fibonacci sequence
    fibonacci_sequence = fibonacci_module.generate_fibonacci(n)

    # Display the generated Fibonacci sequence
    print(f"Fibonacci Sequence of length {n}: {fibonacci_sequence}")


if __name__ == "__main__":
    main()
