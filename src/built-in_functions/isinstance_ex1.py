v=2
print(isinstance(v, int))            # True
print(isinstance(v, str))            # False
print(isinstance(v, list))           # False
print(isinstance(v, (int,str,list))) # True
