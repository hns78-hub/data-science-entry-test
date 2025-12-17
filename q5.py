def check_divisibility(num, divisor):
    # Check if both inputs are numbers
    if type(num) != int and type(num) != float:
        return False
    if type(divisor) != int and type(divisor) != float:
        return False

    # Check divisibility using modulus operator
    if num % divisor == 0:
        return True
    else:
        return False


# Task 2: Call the function
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
