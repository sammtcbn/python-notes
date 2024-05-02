import subprocess

def main():

    cmd = ["bash","-c", "date"]

    try:
        output = subprocess.check_output (cmd, shell=False)
        print(output)
    except Exception as e:
        print(f"An exception occurred: {e}")

    try:
        # Note: output is not string type, so it will fail here.
        if(output.find("2024") >= 0):
            print("found")
        else:
            print("not found")
    except Exception as e:
        print(f"An exception occurred: {e}")

    outputDecodedStr = output.decode()
    print(outputDecodedStr)

    try:
        if(outputDecodedStr.find("2024") >= 0):
            print("found")
        else:
            print("not found")
    except Exception as e:
        print(f"An exception occurred: {e}")

if __name__ == '__main__':
    main()

"""
Result:

$ python ex2.py
b'Thu May  2 05:07:15 PM CST 2024\n'
An exception occurred: argument should be integer or bytes-like object, not 'str'
Thu May  2 05:07:15 PM CST 2024

found

"""
