#int(input('Please enter numbers to find negative numbers in tuple'))
given_tuple = (1, 2,-4,-56,00)

negative_numbers = []
print("Negative Numbers in given Tuple: ")
for each in given_tuple:
    if each < 0:
        negative_numbers.append(each)
print(negative_numbers)
