v = 1

def func1():
    v = 2
    b = 3
    print ("v = ", v)
    print ("Local variables:", locals())

def func2():
    print ("v = ", v)
    print ("Local variables:", locals())

def func3():
    global v
    print ("v = ", v)

def main():
    func1() # 2
            # Local variables: {'v': 2, 'b': 3}

    func2() # 1
            # Local variables: {}

    func3() # 1

    print ("Global variables:", globals())

if __name__ == '__main__':
    main()

