import string

str1 = "Hello, World"
print(str1.startswith("He"))  # True
print(str1.startswith("H"))   # True
print(str1.startswith("ell")) # False

print(str1.endswith("rld"))   # True
print(str1.endswith("d"))     # True
print(str1.endswith("123"))   # False


str2 = "Ubuntu"
# use tuple as parameter
#print(str2.startswith("Centos", "Ubuntu", "SUSE")) # this will fail, below is correct usage for tuple
print(str2.startswith(("Centos", "Ubuntu", "SUSE"))) # True

