lst1 = [1,2,3,4,5]
lst2 = [1, 'hello', 2.3]
lst3 = list (["sam", "jerry", "candy"])
lst4 = list('World')
lst5 = [1, ['sam', 'jerry', 'candy'] , [2, 3, 4]]

print(lst1)
print(lst2)
print(lst3)
print(lst4)
print(lst5)
print(lst2, lst3, lst4)
print('lst5:' + str (lst5))
print(lst1[2])
print(lst1[-1])
print(lst1[-2])

lst1[-1] = 6
print(lst1[-1])

lst1[-1]="Python"
print(lst1)

for e in lst1:
    print(e, end=' ')  

print('\n')
print("append");
lst1.append(7)
print(lst1)

print("extend")
lst1.extend([8,9,10])
print(lst1)

print("insert")
lst1.insert(2,7)
print(lst1)

print("del")
del lst1[0]
print(lst1)

print("pop")
v=lst1.pop()
print ("pop value is " , v)
print(lst1)

print("pop idx 3")
v2=lst1.pop(3)
print ("pop value is " , v2)
print(lst1)

print("remove value 7")
lst1.remove(7)
print(lst1)

print("remove value 7")
lst1.remove(7)
print(lst1)

print("remove value python")
lst1.remove("Python")
print(lst1)

lst6= [3,6,7,1,2]
print("lst6 = ", lst6)

print("soft lst6")
lst6.sort()
print("lst6 = ", lst6)

print("reverse")
lst6.reverse()
print("lst6 = ", lst6)

v7=sum(lst6)
print("sum = ", v7)
