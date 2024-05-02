def main():
    str1="111   222    333 44"
    str1Parts = str1.split()
    for a in str1Parts:
        print(a)

    print(f"parts[0] is {str1Parts[0]}")
    print(f"parts[1] is {str1Parts[1]}")
    print(f"parts[2] is {str1Parts[2]}")
    print(f"parts[3] is {str1Parts[3]}")

    try:
        print(f"parts[4] is {str1Parts[4]}")
    except Exception as e:
        print(f"An exception occurred: {e}")

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
parts[0] is 111
parts[1] is 222
parts[2] is 333
parts[3] is 44
An exception occurred: list index out of range
ab
cdef
ghijkl
mno

"""
