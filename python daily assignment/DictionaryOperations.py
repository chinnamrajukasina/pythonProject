# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Accessing values
name = my_dict['name']
age = my_dict['age']
print(f"Name: {name}, Age: {age}")

# Modifying values
my_dict['age'] = 26
my_dict['city'] = 'San Francisco'

# Print the dictionary after modification
print("Dictionary after Modification:", my_dict)

# Adding a new key-value pair
my_dict['occupation'] = 'Software Engineer'

# Print the dictionary after adding a new key-value pair
print("Dictionary after Adding 'occupation':", my_dict)

# Removing a key-value pair
removed_value = my_dict.pop('city')

# Print the dictionary after removing 'city'
print("Dictionary after Removing 'city':", my_dict)
print("Removed Value:", removed_value)

# Iterating over keys and values
print("Iterating over Keys and Values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Check if a key is present
if 'age' in my_dict:
    print("Key 'age' is present in the dictionary.")
else:
    print("Key 'age' is not present in the dictionary.")
