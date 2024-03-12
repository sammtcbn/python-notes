import subprocess

def main():

    cmd = "date"

    try:
        exit_code, output = subprocess.getstatusoutput (cmd)

        if exit_code == 0:
            print("Execute '{}' successful".format(cmd))
            print("output is " + output)
        else:
            print("Execute '{}' fail".format(cmd))
            print(f"Execution failed with exit code: {exit_code}")

    except Exception as e:
        print(f"An exception occurred: {e}")

if __name__ == '__main__':
    main()
