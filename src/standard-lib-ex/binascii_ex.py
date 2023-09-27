import binascii

str = '12345'

tmp = [0xaa, 0xbb, 0x12, 0x13, 0x14]

def main():
    print(binascii.hexlify(bytearray(str.encode('ascii'))))
    # b'3132333435'

    print(binascii.hexlify(bytearray(tmp)))
    # b'aabb121314'

if __name__ == '__main__':
    main()
