generator_of_strings = ("Number: " + str(i) for i in range(1, 4))

print(type(generator_of_strings))

for tmp in generator_of_strings:
    print(tmp)

## try to join generator
str1=", ".join(generator_of_strings)
print(str1)
# However, it's important to note that in the previous for loop,
# the generator has been fully iterated over, so by the time join is called,
# generator_of_strings is exhausted and no new strings are generated.
# Therefore, str1 ends up as an empty string.

"""
Result:

<class 'generator'>
Number: 1
Number: 2
Number: 3

"""
