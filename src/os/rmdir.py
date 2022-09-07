import sys
import os

def main():
    pathname='/tmp/test123'
    try:
        os.rmdir(pathname)
        print(pathname + " deleted")
    except:
        print("fail to delete " + pathname)
    print("bye")

main()

