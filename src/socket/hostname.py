import socket

def get_hostname():
    try:
        hostname = socket.gethostname()
        return hostname
    except:
        return "NotFound"

print("hostname:", get_hostname())

