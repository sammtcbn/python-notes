import os, sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Example:
    > $python3 argparse_ex1.py -u sam -p 1234 -i 192.168.0.3 -f abc.bin
''')

    parser.add_argument('-u', dest='userid',   required=True,  help='User login id string')
    parser.add_argument('-p', dest='password', required=False, help='User login password string')
    parser.add_argument('-i', dest='serverip', required=True,  help='Server ip string')
    parser.add_argument('-f', dest='filename', required=True,  help='Filename string')

    args = parser.parse_args(sys.argv[1:])

    uid = args.userid
    upw = args.password
    sip = args.serverip
    fn  = args.filename

    print("id = {}, password = {}, ip = {}, file = {}".format(uid, upw, sip, fn))

if __name__ == '__main__':
    main()
