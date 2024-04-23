def main():
    str1="111   222    333 44"
    str1Parts = str1.split()
    for a in str1Parts:
        print(a)

    str2="ab;cdef;ghijkl;mno"
    str2Arr = str2.split(";")
    for a in str2Arr:
        print(a)

if __name__ == '__main__':
    main()

"""
Result:

111
222
333
44
ab
cdef
ghijkl
mno

"""
