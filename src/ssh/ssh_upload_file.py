# pip install paramiko
import paramiko

def update_file_to_ssh_server(ip, user, pwd, fn, destdir):
    ret = False

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print("Connecting to {}".format(ip))
        ssh.connect(ip, username=user, password=pwd)
        channel = ssh.invoke_shell()
        if channel:
            sftp = ssh.open_sftp()
            dest_filename = '{}/{}'.format(destdir, fn)
            sftp.put(fn, dest_filename)
            sftp.close()            
            print("upload file {} to folder {}".format(fn, destdir))
            ret = True
    except Exception as e:
        print(e)

    return ret

def main():
    serverip = "192.168.0.4"
    userid = "sam"
    userpwd = "1234"
    myfile = "report.txt"
    destdir = "/tmp"
    update_file_to_ssh_server(serverip, userid, userpwd, myfile, destdir)

if __name__ == '__main__':
    main()
