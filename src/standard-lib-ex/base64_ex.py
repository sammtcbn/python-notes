import base64

str = '12345'

def convert_str_to_base64_ascii(input_str):
    ascii_bytes = input_str.encode('ascii')
    base64_bytes = base64.b64encode(ascii_bytes)
    return base64_bytes

def main():
    output = convert_str_to_base64_ascii (str)
    print (output)

if __name__ == '__main__':
    main()
