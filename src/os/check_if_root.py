import os
import sys

def check_if_root():
    # Get the effective user ID (UID) of the current process
    user_id = os.geteuid()

    # Root user typically has a UID of 0
    if user_id == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    if check_if_root() == False:
        print("Current user is not root. Exiting program.")
        sys.exit(1)
    print("Current user is root.")
    print("bye")

"""
Result:

$ python check_if_root.py
Current user is not root. Exiting program.

$ sudo python check_if_root.py
[sudo] password for sam:
Current user is root.
bye
"""
