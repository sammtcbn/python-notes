import subprocess

def get_ipaddr_by_macaddr_using_arp(macaddr):
    # method 1
    # cmd = "arp -n | grep {} | sort -u | awk '{{print $1}}'".format(macaddr)

    # method 2
    # arp -n | awk '/11:22:33:44:55:66/ {print $1;exit}'
    cmd = "arp -n | awk '/{}/ {{print $1 ;exit}}'".format(macaddr)

    #print("cmd is {}".format(cmd))
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
    ipaddr=get_ipaddr_by_macaddr_using_arp(macaddr)
    if ipaddr:
        print("ip addr is:{}".format(ipaddr))
    else:
        print("not found")

if __name__ == '__main__':
    main()
