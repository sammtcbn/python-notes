v1 = {
   1: 'apple',
   2: 'banana'
}

v2 = dict([('apple', 'sam'), ('fb', 'joe'), ('telsa', 'vicky')])


print("v1=" , v1)
print("v2=" , v2)

print("change fb value to vivian")
v2["fb"]='vivian'
print("v2=" , v2)

print("add a non-exist key, microsoft")
v2["microsoft"]='gigi'
print("v2=" , v2)

print("foreach show key and value")
for com in v2:
   employeename=v2[com]
   print(com, employeename, end=' ')

print("\n")

print("del key=fb")
del v2["fb"]
print("v2=" , v2)

print("pop")
e1 = v2.pop('apple')
print("pop apple, value is ", e1)
print("v2=" , v2)

print("random pop")
e2 = v2.popitem()
print("popitem, value is ", e2)
print("v2=" , v2)

