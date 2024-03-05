import hashlib
import sys

def append_binary(file_path, threshold_size):
    try:
        with open(file_path, 'rb') as file:
            original_content = file.read()

        if len(original_content) < threshold_size:
            padding_size = threshold_size - len(original_content)
            padding_content = bytes([0xFF] * padding_size)
            new_content = original_content + padding_content
        else:
            new_content = original_content

        return new_content

    except FileNotFoundError:
        print(f'File "{file_path}" not found。')

def compute_sha384(buf):
    sha384_hash = hashlib.sha384(new_content).hexdigest()
    print(f'{sha384_hash}')

if len(sys.argv) != 2:
    print('Please assign file')
else:
    file_path = sys.argv[1]
    new_content = append_binary(file_path, 0x80000)
    compute_sha384(new_content)
