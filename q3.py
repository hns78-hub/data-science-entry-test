def update_dictionary(dct, key, value):
    # Check if dct is a dictionary
    if type(dct) != dict:
        return -1

    # Check if the key already exists
    if key in dct:
        print("Original value:", dct[key])

    # Update or add the key-value pair
    dct[key] = value

    return dct


# Task 2: Call the function
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))
