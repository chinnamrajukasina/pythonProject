given_number = int(input('Enter the number to find Prime or not: '))

count = 0
for x in range(1, given_number + 1):
    if given_number % x == 0:
        count += 1
if count == 2:
    print("given number is a prime number :", given_number)
else:
    print("given number is not a prime number :", given_number)
