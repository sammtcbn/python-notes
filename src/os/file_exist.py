import os

files = (os.getcwd(), "file_exist.py")

for f in files:
    print ("item = " + str (f))
    if os.path.exists(f):
        print ("exist")
    if os.path.isdir (f):
        print ("is directory")
    if os.path.isfile (f):
        print ("is file")
