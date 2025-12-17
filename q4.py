def string_reverse(s):
    # Check if s is a string
    if type(s) != str:
        return -1

    # Start with an empty string
    reversed_string = ""

    # Go through the string one character at a time
    for char in s:
        reversed_string = char + reversed_string

    return reversed_string


# Task 2: Call the function
print(string_reverse("Hello World"))
print(string_reverse("Python"))
