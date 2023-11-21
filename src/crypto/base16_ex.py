import base64

str = '12345'

def convert_str_to_base16_ascii(input_str):
    ascii_bytes = input_str.encode('ascii')
    base16_bytes = base64.b16encode(ascii_bytes)
    return base16_bytes

def main():
    output = convert_str_to_base16_ascii (str)
    print (output)

if __name__ == '__main__':
    main()
