str1="Hello"
print(str1.isalnum())
print(str1.isalpha())
print(str1.isidentifier())
print(str1.isupper())
print(str1.isspace())
print(str1.islower())
print(str1.isdigit())
print(max(str1))
print(min(str1))

str2="123"
print(str2.isdigit())
print(len(str2))

str3="ab;cdef;ghijkl;mno"
str3Arr = str3.split(";")
for a in str3Arr:
    print(a)

''' Result:

$ python3 str_func.py
True
True
True
False
False
False
False
o
H
True
3
ab
cdef
ghijkl
mno

'''
