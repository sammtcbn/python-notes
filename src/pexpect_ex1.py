# pip3 install pexpect
import pexpect

def main():
    process = pexpect.spawn('nslookup')
    process.expect('>')
    process.sendline('www.google.com')
    process.expect('>')
    print(process.before.decode())
    process.sendline('exit')

if __name__ == '__main__':
    main()
