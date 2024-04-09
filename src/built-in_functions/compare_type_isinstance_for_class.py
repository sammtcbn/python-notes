# refer to https://www.runoob.com/python/python-func-isinstance.html
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # True
print(isinstance(B(), A))  # True

print(type(A()))           # <class '__main__.A'>
print(type(B()))           # <class '__main__.B'>

print(type(A()) == A)      # True
print(type(B()) == A)      # False
