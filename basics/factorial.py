def factorial(nbr):
    fact = 1
    for itr in range(1, nbr + 1):
        fact = fact * itr
    return fact


n = int(input("Enter the number to find Factorial of that number :"))

print(factorial(n))
