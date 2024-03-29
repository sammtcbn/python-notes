from get_linux_distribution import get_linux_distribution

def get_package_manager(distribution):
    if distribution.lower() in ['debian', 'ubuntu']:
        return 'apt'
    elif distribution.lower() in ['rhel', 'centos', 'fedora']:
        #return 'yum/dnf'
        return 'yum'
    else:
        return None


def main():
    distribution_name = get_linux_distribution()

    if distribution_name:
        package_manager = get_package_manager(distribution_name)
        if package_manager:
            print(f"The package manager for {distribution_name} is: {package_manager}")
        else:
            print(f"No package manager found for {distribution_name}.")
    else:
        print("Unable to determine the Linux distribution.")


if __name__ == '__main__':
    main()


# Result:

# python get_linux_package_manager.py
# The package manager for Ubuntu is: apt
