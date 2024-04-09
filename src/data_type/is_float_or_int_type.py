# refer to https://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file-in-python

def is_float_str (string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_int_str (string: str) -> bool:
    try:
        int(string)
        return True
    except ValueError:
        return False

def main():
    print(is_float_str("12"))     # True
    print(is_int_str("12"))       # True

    print(is_float_str("12.34"))  # True
    print(is_int_str("12.34"))    # False

    print(is_float_str("abc"))    # False
    print(is_int_str("abc"))      # False

if __name__ == '__main__':
    main()
