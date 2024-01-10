import sys

print(sys.version_info[0]) # 3
print(sys.version_info[1]) # 11
print(sys.version_info[2]) # 6
print(sys.version_info)    # sys.version_info(major=3, minor=11, micro=6, releaselevel='final', serial=0)

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

print("running python version greater than 3")


# $ python3 --version
# Python 3.11.6
