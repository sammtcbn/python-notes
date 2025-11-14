import zlib, sys

with open(sys.argv[1], "rb") as f:
    data = f.read()

print(format(zlib.crc32(data) & 0xffffffff, "08X"))

