def hexshow(str):
    result = ''
    hlen = len(str)
    for i in range(hlen):
        val = ord(str[i])
        tmphex = '%02x'%val
        result += tmphex + ' '
    print(result)

def main():
    hexshow('1234 abcd ABCD')

if __name__ == '__main__':
    main()

# Result:

# $ python hexshow.py
# 31 32 33 34 20 61 62 63 64 20 41 42 43 44
