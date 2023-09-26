import base64

str = '12345'

def convert_str_to_base32_ascii(input_str):
    ascii_bytes = input_str.encode('ascii')
    base32_bytes = base64.b32encode(ascii_bytes)
    return base32_bytes

def main():
    output = convert_str_to_base32_ascii (str)
    print (output)

if __name__ == '__main__':
    main()
