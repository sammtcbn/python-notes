bar = 200

def foo():
    global bar
    bar += 1
    print(bar) # 201

foo()
