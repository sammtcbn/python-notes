# refer to https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
import re

def remove_ansi_escape_7bit_sequences(str):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    result = ansi_escape.sub('', str)
    return result

def remove_ansi_escape_8bit_sequences(str):
    ansi_escape = re.compile(br'(?:\x1B[@-Z\\-_]|[\x80-\x9A\x9C-\x9F]|(?:\x1B\[|\x9B)[0-?]*[ -/]*[@-~])')
    result = ansi_escape.sub(b'', str)

def main():
    mytext = 'ls\r\n\x1b[00m\x1b[01;31mexamplefile.zip\x1b[00m\r\n\x1b[01;31m'

    strfixed = remove_ansi_escape_7bit_sequences(mytext)
    print(strfixed)

if __name__ == '__main__':
    main()
