# pip3 install psutil
import psutil

def main():
    cpucnt_logical = psutil.cpu_count()
    print("Logical CPU count is", cpucnt_logical)

    cpucnt_physical = psutil.cpu_count(logical=False)
    print("Physical CPU core count is", cpucnt_physical)

if __name__ == '__main__':
    main()

"""
Result:

$ python psutil_ex1.py
Logical CPU count is 8
Physical CPU core count is 4
"""
