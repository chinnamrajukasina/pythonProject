def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Input temperature and unit from the user
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert temperatures
if unit.upper() == 'C':
    converted_temperature = celsius_to_fahrenheit(temperature)
    print(f"{temperature} Celsius is equal to {converted_temperature} Fahrenheit.")
elif unit.upper() == 'F':
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} Fahrenheit is equal to {converted_temperature} Celsius.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
