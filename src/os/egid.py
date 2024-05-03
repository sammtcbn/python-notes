import os

egid=os.getegid()
print("The effective group id of the current process:", egid)

"""
Result:

$ python egid.py
The effective group id of the current process: 1000

$ sudo python egid.py
The effective group id of the current process: 0

"""
