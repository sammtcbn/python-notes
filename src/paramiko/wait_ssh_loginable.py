# pip install paramiko
import paramiko
import time

def wait_ssh_loginable(ip, username, password, retries=10, delay=5):
    for attempt in range(retries):
        try:
            # Create an SSH client
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Try to connect to the target IP
            ssh.connect(ip, username=username, password=password, timeout=10)
            
            # Execute the echo command
            stdin, stdout, stderr = ssh.exec_command("echo 'SSH Connection Successful'")
            output = stdout.read().decode()
            
            # Close the SSH connection
            ssh.close()
            
            if 'SSH Connection Successful' in output:
                return 0
        except Exception as e:
            print(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    
    return 1

def main():
    ip = "192.168.1.2"
    username = "sam"
    password = "1234"
    result = wait_ssh_loginable(ip, username, password)
    print("Result:", result)

if __name__ == '__main__':
    main()
