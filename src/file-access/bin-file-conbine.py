import random

def main():
    with open("src.bin", "wb+") as sfile:
        random_buffer = bytes([random.randint(0, 255) for _ in range(1024)])
        sfile.write(random_buffer)

    with open("src.bin", "rb+") as sfile:
        readtmp = sfile.read()

    with open("dest.bin", "wb+") as dfile:
        dfile.seek(0)
        dfile.write(b'\xFF'*8*1024*1024)
        dfile.seek(0x400000)
        dfile.write(readtmp)

if __name__ == "__main__":
    main()
