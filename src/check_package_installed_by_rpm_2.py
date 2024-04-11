import sys
import subprocess
from check_command_exists import check_command_exists

def check_package_installed_by_rpm(package_name):
    try:
        subprocess.check_output(['rpm', '-qi', package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def check_package(package_name):
    if check_package_installed_by_rpm(package_name) is False:
        print("{} is not installed".format(package_name))
    else:
        print("{} is installed".format(package_name))

def main():
    if check_command_exists('rpm') is False:
        print("rpm command doesn't exist")
        sys.exit(1)

    check_package('git')
    check_package('nmap')
    check_package('net-snmp')

if __name__ == '__main__':
    main()
