import subprocess

def check_command_exists(command):
    try:
        subprocess.run(['which', command], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def check_cmd(command):
    if check_command_exists(command):
        print("{} exists".format(command))
    else:
        print("{} doesn't exist".format(command))

def main():
    check_cmd('ls')
    check_cmd('who')
    check_cmd('dpkg')
    check_cmd('rpm')

if __name__ == '__main__':
    main()

"""
Result:

$ python check_command_exists.py
ls exists
who exists
dpkg exists
rpm doesn't exist
"""
