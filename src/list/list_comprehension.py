mylist=[i for i in range(0,9)]
print(mylist)        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(type(mylist))  # <class 'list'>

mylist2=[i for i in range(0,9) if i not in [2,5,7]]
print(mylist2)       # [0, 1, 3, 4, 6, 8]
print(type(mylist2)) # <class 'list'>
