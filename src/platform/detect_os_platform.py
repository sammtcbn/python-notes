import platform

os = platform.system()
print("Current OS: ", os)

# Will show Linux or Windows


if os == "Linux":
    print("test in Linux")
elif os == "Windows":
    print("test in Windows")
else:
    print("Unsupported Platform")

print("release:  ", platform.release())
print("version:  ", platform.version())
print("platform: ", platform.platform())
