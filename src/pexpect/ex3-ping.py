import pexpect
import sys
import time

cmd="ping 8.8.8.9"
expected_string = "64 bytes from 8.8.8.8: icmp_seq="
global_timeout = 60  # Timeout in seconds
start_time = time.time()

def main():
    p = pexpect.spawn(cmd, encoding="utf-8")
    while True:
        if (time.time() - start_time) >= global_timeout:
            print("Timeout: '", expected_string, "' not received within", global_timeout, "seconds.")
            break

        print("expect ...")
        index = p.expect([expected_string, pexpect.EOF, pexpect.TIMEOUT], timeout=1)
        if index == 0:
            print("got")
            break

if __name__ == '__main__':
    main()
