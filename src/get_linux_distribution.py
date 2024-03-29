def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('NAME='):
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        pass  # If the file doesn't exist or inaccessible, return None

    return None


def get_linux_distribution_and_version():
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('PRETTY_NAME='):
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        pass  # If the file doesn't exist or inaccessible, return None

    return None


def main():
    distribution_name = get_linux_distribution()
    if distribution_name:
        print(f"The current Linux distribution is: {distribution_name}")
    else:
        print("Unable to determine the Linux distribution.")

    distribution_name_ver = get_linux_distribution_and_version()
    if distribution_name_ver:
        print(f"The current Linux distribution is: {distribution_name_ver}")
    else:
        print("Unable to determine the Linux distribution.")


if __name__ == '__main__':
    main()

# Result:

# python get_linux_distribution.py
# The current Linux distribution is: Ubuntu
# The current Linux distribution is: Ubuntu 23.10
