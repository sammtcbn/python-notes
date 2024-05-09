import os

print(os.environ)

user = os.environ.get('USER')
print(user) # sam

xyz = os.environ.get('XYZ')
print(xyz)  # None

xyz = os.environ.get('XYZ', 'default_value')
print(xyz)  # default_value
