class PowerCalculator:
    def power(self, x, n):
        if not isinstance(n, int):
            raise ValueError("Exponent must be an integer.")

        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        current_power = x

        while n > 0:
            if n % 2 == 1:
                result *= current_power
            current_power *= current_power
            n //= 2

        return result


# Example usage:
if __name__ == "__main__":
    try:
        base = float(input("Enter the base (x): "))
        exponent = int(input("Enter the exponent (n): "))

        calculator = PowerCalculator()
        result = calculator.power(base, exponent)

        print(f"{base}^{exponent} = {result}")
    except ValueError as ve:
        print(f"Error: {ve}")
