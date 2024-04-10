import sys
import os

progname = "template"
progver = "1.0.0"

def main():
    workdir = os.getcwd()
    print(progname + " v" + progver)
    print("workdir - " + workdir)

if __name__ == '__main__':
    main()
