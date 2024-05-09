import platform

def get_hostname():
    try:
        hostname = platform.node()
        return hostname
    except:
        return "NotFound"

print("hostname:", get_hostname())
