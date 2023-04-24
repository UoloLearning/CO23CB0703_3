def calculation(a, b):
    add_result = a + b
    sub_result = a - b
    return add_result, sub_result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

addition, subtraction = calculation(num1, num2)

print("The addition result is:", addition)
print("The subtraction result is:", subtraction)
