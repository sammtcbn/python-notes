import shutil

def main():
    src="read.txt"
    dst="read-copy.txt"
    shutil.copyfile(src, dst)

if __name__ == "__main__":
    main()
