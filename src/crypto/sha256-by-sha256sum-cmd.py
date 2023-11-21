import sys
import subprocess

def calculate_sha256(filename):
    cmd = "sha256sum {}".format(filename)
    print("cmd = {}".format(cmd))
    try:
        status, output = subprocess.getstatusoutput(cmd)
    except Exception as e:
        print("Execute '{}' has exception: {}".format(cmd, e))
        sys.exit(1)

    print("output = {}".format(output))
    if status != 0:
        print("!!! Execute '{}' fail.".format(cmd))
        sys.exit(1)

    resp = output.split(" ")
    print("resp = {}".format(resp[0]))
    sha256_sum = resp[0]
    return sha256_sum

def main():
    filename = "your_file_name_here"
    result = calculate_sha256(filename)
    print(f"The SHA256 hash of the file '{filename}' is: {result}")

main()
