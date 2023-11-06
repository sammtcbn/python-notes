# generates a random data file with a specified size in high speed
# numpy is needed:  pip install numpy
# You can run this program from the command line and specify the file name and size as follows:
# python generate_random_file.py my_random_data.bin 1024
# This command will generate a binary file named my_random_data.bin with a size of 1024 bytes.
# You can adjust the file name and size as needed.

import os
import random
import argparse
import numpy as np

def generate_random_file(file_path, file_size_in_bytes):
    random_data = np.random.bytes(file_size_in_bytes)
    with open(file_path, 'wb+') as file:
            file.write(random_data)

def main():
    parser = argparse.ArgumentParser(description='Generate a random data file with a specified size.')
    parser.add_argument('file_path', help='Path to the output file')
    parser.add_argument('file_size', type=int, help='Size of the output file in bytes')

    args = parser.parse_args()
    generate_random_file(args.file_path, args.file_size)
    print(f"File generated: {args.file_path}, size: {os.path.getsize(args.file_path)} bytes")

if __name__ == "__main__":
    main()
