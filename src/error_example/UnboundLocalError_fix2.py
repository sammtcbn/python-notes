bar = 200

def foo():
    bar = 0  # initial var as a local var
    bar += 1
    print(bar) # 1

foo()
print(bar) # 200
