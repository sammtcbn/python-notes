# Note:
# https://docs.python.org/3/library/random.html
# random.randrange(stop)
# random.randrange(start, stop[, step])
#    Return a randomly selected element from range(start, stop, step).

import random

for i in range(10):
    print(random.randrange(1,10,2))

print("===")

for i in range(10):
    print(random.randrange(2,10,2))

print("===")

for i in range(10):
    print(random.randrange(1,10,3))

"""
Result:

$ python randrange.py
5
3
9
7
7
3
7
1
9
7
===
8
8
2
6
2
8
4
6
4
4
===
1
1
1
4
7
7
4
1
7
1

"""
