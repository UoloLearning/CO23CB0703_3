def factorial(n):
    """This function calculates the factorial of a number."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
