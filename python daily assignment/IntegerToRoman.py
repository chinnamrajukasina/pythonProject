class IntegerToRoman:
    def __init__(self):
        self.numeral_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

    def convert_to_roman(self, num):
        if not isinstance(num, int) or not 1 <= num <= 3999:
            raise ValueError("Input must be an integer between 1 and 3999.")

        result = ""
        for value, symbol in sorted(self.numeral_map.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += symbol
                num -= value

        return result

# Example usage:
if __name__ == "__main__":
    try:
        integer_value = int(input("Enter an integer (1 to 3999): "))
        converter = IntegerToRoman()
        roman_numeral = converter.convert_to_roman(integer_value)
        print(f"The Roman numeral representation: {roman_numeral}")
    except ValueError as ve:
        print(f"Error: {ve}")

