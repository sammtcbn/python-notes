import sys
import os

def myfun(pathname):
    if not os.path.exists(pathname):
        print(pathname + " not exist")
        try:
            os.makedirs(pathname)
            print(pathname + " created")
        except:
            print(pathname + " created fail") 
    else:
        print(pathname + " exist")

def main():
    path1='/tmp/test123'
    path2='/opt/test456'
    myfun(path1)
    myfun(path2)
    print("done")

main()

# Result:

# $ python3 mkdir.py
# /tmp/test123 not exist
# /tmp/test123 created
# /opt/test456 not exist
# /opt/test456 created fail
# done
