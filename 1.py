def swap(x, y):
    # Check if x and y are numbers
    if type(x) != int and type(x) != float:
        return -1
    if type(y) != int and type(y) != float:
        return -1

    # Swap the values
    temp = x
    x = y
    y = temp

    print("x =", x)
    print("y =", y)


# Task 2: Call the function
print(swap("Apple", 10))  # Not numeric
print()
swap(9, 17)               # Numeric
