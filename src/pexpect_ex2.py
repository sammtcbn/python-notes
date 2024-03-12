# pip3 install pexpect
import pexpect

def main():
    process = pexpect.spawn('ls -l')
    process.expect(pexpect.EOF)
    result = process.before.decode()
    print(result)

if __name__ == '__main__':
    main()
