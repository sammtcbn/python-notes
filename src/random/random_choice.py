import random

str1 = "Hello World"
print(random.choice(str1))

list1 = [1,2,3,4,5]
print(random.choice(list1))

list2 = ["Vue", "Angular", "React"]
print(random.choice(list2))

tuple1 = ("Vue", "Angular", "React")
print(random.choice(tuple1))

set1 = {"Vue", "Angular", "React"}
#print(random.choice(set1))         # TypeError: 'set' object is not subscriptable

# generate a random number between 0 and 9, exclude 2, 5, 7
print(random.choice([i for i in range(0,9) if i not in [2,5,7]]))
