import subprocess

def main():

    cmd = "date"

    try:
        status, output = subprocess.getstatusoutput (cmd)
    except Exception as e:
        print(e)

    print (status)
    print ("output is " + output)

    if status != 0:
        print("Execute '{}' fail".format(cmd))
    else:
        print("Execute '{}' pass".format(cmd))

if __name__ == '__main__':
    main()
