import sys
import os

def main():
    newpath="/tmp"

    path=os.getcwd()
    print("current path - " + path)

    print("going to change to " + newpath)
    try:
        os.chdir (newpath)
    except:
        print("fail to change to " + newpath)

    path=os.getcwd()
    print("current path - " + path)

    print("bye")

main()

