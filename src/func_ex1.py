v = 1

def print_msg():
    print ("Hello World")

def empty_func():
    pass

def sum_func(arg1, arg2):
    sum=0
    sum=arg1+arg2
    return sum

def cal_func(argc, arg2):
    return argc+1, arg2+1

def cal2_func(argc=5, arg2=10):
    return argc+1, arg2+1

def inc():
    global v
    v=v+1
    return v

print_msg()
empty_func
print ("sum = ", sum_func(3,5))
print ("cal = ", cal_func(3,5))
print ("cal = ", cal2_func(3))
print ("gVal = ", inc())

