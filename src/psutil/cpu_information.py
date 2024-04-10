# pip3 install psutil
import psutil

def main():
    print(psutil.cpu_freq())
    print(psutil.cpu_stats())
    print(psutil.cpu_times())
    print(psutil.cpu_percent())

if __name__ == '__main__':
    main()

"""
Result:

$ python cpu_information.py
scpufreq(current=1617.973, min=800.0, max=2500.0)
scpustats(ctx_switches=2228601926, interrupts=1672765478, soft_interrupts=1071958245, syscalls=0)
scputimes(user=77037.95, nice=1808.79, system=106660.52, idle=32367870.04, iowait=1247.85, irq=0.0, softirq=12897.37, steal=0.0, guest=0.0, guest_nice=0.0)
50.0
"""
