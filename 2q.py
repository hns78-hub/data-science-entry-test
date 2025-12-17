def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Search for all occurrences of find_val in lst
    - Replace them with replace_val
    - lst must be a list
    - Return the modified list
    """

    # Check if lst is a list
    if type(lst) != list:
        return -1

    # Go through the list and replace values
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst


# Task 2: Function calls
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
