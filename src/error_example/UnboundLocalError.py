bar = 200

def foo():
    bar += 1

foo()

"""
Result:

UnboundLocalError: cannot access local variable 'bar' where it is not associated with a value

"""
