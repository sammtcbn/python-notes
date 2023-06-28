import sys
import os

progname = "template"
progver = "1.0.0"

workdir = os.getcwd()

def main():
    print(progname + " v" + progver)
    print("workdir - " + workdir)

main()
