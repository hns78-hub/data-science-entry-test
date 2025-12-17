def find_first_negative(lst):
    # Start from the first index
    i = 0

    # Loop through the list using while
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i = i + 1

    # If no negative number is found
    return "No negatives"


# Task 2: Call the function
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0])
