# Purpose: just use dd and hexdump to read data from device and convert data in hex string
import subprocess

def readDeviceDataHex(devicenode, startaddr, length):
    # dd if=/dev/mtd0 bs=1 skip=0 count=100 2>/dev/null | hexdump -v -e '1/1 "%02x"'
    cmd = f"dd if={devicenode} bs=1 skip={startaddr} count={length} 2>/dev/null | hexdump -v -e '1/1 \"%02x\"'"
    print("cmd=",cmd)

    try:
        exit_code, output = subprocess.getstatusoutput (cmd)

        if exit_code == 0:
            print("Execute '{}' successful".format(cmd))
            print("output is " + output)
            if len(output) < 1:
                return None
            return output
        else:
            print("Execute '{}' fail".format(cmd))
            print(f"Execution failed with exit code: {exit_code}")
            return None

    except Exception as e:
        print(f"An exception occurred: {e}")
        return None

def main():
    datastr = readDeviceDataHex ("/dev/mtd0", 0, 100)
    if datastr != None:
        print("datastr=", datastr)
    else:
        print("read fail!")

if __name__ == '__main__':
    main()

""" Result:

cmd= dd if=/dev/mtd0 bs=1 skip=0 count=100 2>/dev/null | hexdump -v -e '1/1 "%02x"'
Execute 'dd if=/dev/mtd0 bs=1 skip=0 count=100 2>/dev/null | hexdump -v -e '1/1 "%02x"'' successful
output is ffffffffffffffffffffffffffffffff5aa5f00f030004000802101300000000fffffffffffffffffffffffffffffffff5029c64214260adb7b9c4c7ffffffff000000000100fe0eff7f0000ff7f0000ff7f0000ff0efe0fff7f0000ff7f0000ff7f0000
datastr= ffffffffffffffffffffffffffffffff5aa5f00f030004000802101300000000fffffffffffffffffffffffffffffffff5029c64214260adb7b9c4c7ffffffff000000000100fe0eff7f0000ff7f0000ff7f0000ff0efe0fff7f0000ff7f0000ff7f0000

"""