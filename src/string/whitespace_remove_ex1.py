def remove_whitespace(input_string):
    return ''.join(input_string.split())

input_str = "This is a string with whitespace characters"
result_str = remove_whitespace(input_str)

print("Original string:", input_str)
print("String after removing whitespace:", result_str)

