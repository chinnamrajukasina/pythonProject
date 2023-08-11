inputNumber = int(input("Enter the number to find Factorial of that number :"))


def factorial_with_recursion(n):
    if n == 1:
        return 1
    return factorial_with_recursion(n - 1) * n


print(factorial_with_recursion(inputNumber))
