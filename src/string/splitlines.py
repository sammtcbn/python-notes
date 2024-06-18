def main():
    multiline_string="line 11111\nline2222 2\r\nline 33333\r\nline44  444\nline55 555"
    lines = multiline_string.splitlines()
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()

"""
Result:
line 11111
line2222 2
line 33333
line44  444
line55 555
"""
