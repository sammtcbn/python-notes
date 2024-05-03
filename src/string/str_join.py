str1 = "Hello"
str2 = "world"
result = str1 + " " + str2
print(result)                # Hello world


str_list = ["I", "am", "Sam"]
result = " ".join(str_list)
print(result)                # I am Sam


str_list2 = [str1, str2]
str3 = " ".join(str_list2)
print(str3)                  # Hello world


tuple_of_strings = ("Hello", "Sam", "!")
str4 = " ".join(tuple_of_strings)
print(str4)                  # Hello Sam !


set_of_strings = {"Python", "is", "awesome"}
str5 = " ".join(set_of_strings)
# order may vary since sets are unordered
print(str5)                  # is awesome Python
                             # Python awesome is

# use a custom separator to join a string list
str_list3 = ["I", "am", "Sam"]
result = " | ".join(str_list3)
print(result)                # I | am | Sam

