import subprocess

def check_package_installed_by_dpkg(package_name):
    try:
        subprocess.check_output(['dpkg', '-l', package_name])
        return True
    except subprocess.CalledProcessError:
        return False

def check_package(package_name):
    if check_package_installed_by_dpkg(package_name) is False:
        print("{} is not installed".format(package_name))
    else:
        print("{} is installed".format(package_name))

def main():
    check_package('git')
    check_package('nmap')
    check_package('snmp')

if __name__ == '__main__':
    main()

# Result:

# $ python check_package_installed_by_dpkg.py
# git is installed
# nmap is installed
# dpkg-query: no packages found matching snmp
# snmp is not installed

