# pip3 install psutil
import psutil

def main():
    for x in range(5):
        print(psutil.cpu_percent(interval=0.5, percpu=True))

if __name__ == '__main__':
    main()

"""
Result:

$ python cpu_usage.py
[0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

"""
