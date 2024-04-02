import sys
import serial
import pexpect.fdpexpect
import pexpect.popen_spawn


def main():
    try:
        print("Open serial port ...")
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
    except:
        sys.exit ("Error opening port")

    print("Serial port opened")

    session = pexpect.fdpexpect.fdspawn(ser, timeout=10)

    try:
        session.expect('Power On')
        print("got Power On")
        session.expect('System is ready')
        print("got System is ready")
    except Exception as e:
        print(f"An exception occurred: {e}")
        #print(e)

    ser.close()
    print("port is closed")

if __name__ == '__main__':
    main()
    print("bye")
