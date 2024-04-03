import os

def main():
    cmd = "date"
    ret = os.system(cmd)
    if ret == 0:
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    main()
