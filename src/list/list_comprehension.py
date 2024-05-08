# List comprehension (列表推導式)
# https://en.wikipedia.org/wiki/List_comprehension
# https://zh.wikipedia.org/zh-tw/%E5%88%97%E8%A1%A8%E6%8E%A8%E5%AF%BC%E5%BC%8F

mylist=[i for i in range(0,9)]
print(mylist)        # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(type(mylist))  # <class 'list'>

mylist2=[i for i in range(0,9) if i not in [2,5,7]]
print(mylist2)       # [0, 1, 3, 4, 6, 8]
print(type(mylist2)) # <class 'list'>

mylist3=[2*x for x in range(10) if x**2 > 5]
print(mylist3)       # [6, 8, 10, 12, 14, 16, 18]

myset1={v for v in 'ABCDABCD' if v not in 'CB'}
print(myset1)        # {'A', 'D'} , sometimes show {'D', 'A'}
print(type(myset1))  # <class 'set'>
