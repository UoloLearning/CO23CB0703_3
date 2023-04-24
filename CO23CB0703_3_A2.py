def square(num):
    """This function calculates the square of a number."""
    return num ** 2

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Calculate the square of the number using the square function
result = square(num)

# Print the result
print("The square of", num, "is", result)
