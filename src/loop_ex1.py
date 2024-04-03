m=int(input("enter a number:"))
sum=0
for i in range (1, m+1):
    sum=sum+i
    print("i=",i,"sum=",sum)
print("sum=",sum)

"""
Result:

$ python loop_ex1.py
enter a number:10
i= 1 sum= 1
i= 2 sum= 3
i= 3 sum= 6
i= 4 sum= 10
i= 5 sum= 15
i= 6 sum= 21
i= 7 sum= 28
i= 8 sum= 36
i= 9 sum= 45
i= 10 sum= 55
sum= 55
"""
