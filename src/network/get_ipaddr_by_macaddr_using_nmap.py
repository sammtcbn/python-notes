# need root to run

# nmap command reference:
# nmap -sP 192.168.1.0/24 | grep -i 11:22:33:44:55:66 -B2 | grep "Nmap scan report for" | awk 'BEGIN {FS="for"} {print $2}' | sed 's/^[ \t]*//' | grep -Po '\(\K[^)]+(?=\))'

import os
import subprocess

def get_ipaddr_by_macaddr_using_nmap(subnet, macaddr):
    cmd = "nmap -sP  {} | grep -i {} -B2 | grep \"Nmap scan report for\" | awk 'BEGIN {{FS=\"for\"}} {{print $2}}' | sed 's/^[ \\t]*//' | grep -Po '\\(\\K[^)]+(?=\\))'".format(subnet, macaddr)
    #print("cmd is {}".format(cmd))

    if os.geteuid() != 0:
        print("need root priviliedge")
        return None

    try:
        exit_code, output = subprocess.getstatusoutput (cmd)

        if exit_code == 0:
            #print("Execute successful")
            #print("output is " + output)
            if "not found" in output:
                print("command not found")
                return None
            if len(output) < 7:
                return None
            return output
        else:
            print(f"Execution failed with exit code: {exit_code}")
            return None

    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

def main():
    macaddr="11:22:33:44:55:66"
    subnet="192.168.1.0/24"
    ipaddr=get_ipaddr_by_macaddr_using_nmap(subnet, macaddr)
    if ipaddr:
        print("ip addr is:{}".format(ipaddr))
    else:
        print("not found")

if __name__ == '__main__':
    main()
