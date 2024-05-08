# id office doc - https://docs.python.org/3/library/functions.html#id

x=10
y=10
print("x addr is ", id(x)) # 11754184
print("y addr is ", id(y)) # 11754184

y=11
print("x addr is ", id(x)) # 11754184
print("y addr is ", id(y)) # 11754216

