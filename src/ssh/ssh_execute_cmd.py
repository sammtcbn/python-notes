# pip install paramiko
import paramiko

def ssh_run_cmd(ip, user, pwd, cmdstr):
    ret = False

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        print("Connecting to {}".format(ip))
        ssh.connect(ip, username=user, password=pwd)
        channel = ssh.invoke_shell()
        if channel:
            stdin, stdout, stderr = ssh.exec_command(cmdstr)
            ret = True
    except Exception as e:
        print(e)

    return ret

def main():
    serverip = "192.168.0.4"
    userid = "sam"
    userpwd = "1234"
    mycmd = "rm /tmp/report.txt"
    ssh_run_cmd(serverip, userid, userpwd, mycmd)

if __name__ == '__main__':
    main()
