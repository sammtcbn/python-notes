import os
import string

files = os.listdir()
for file in files:
    if file.startswith("str"):
        print(file)
