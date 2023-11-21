import hashlib

def calculate_sha256_range(data, start=0, end=None):
    try:
        if end is None:
            end = len(data)
        sha256_hash = hashlib.sha256(data[start:end+1]).hexdigest()
        return sha256_hash
    except Exception as e:
        return f"Error calculating SHA256: {str(e)}"

def main():
    filename = "your_file_name_here"

    with open(filename, 'rb') as f:
        data = bytearray(f.read())
    
    start_pos = 0
    end_pos   = None
    result = calculate_sha256_range(data, start_pos, end_pos)
    print(f"The SHA256 hash of the all content is: {result}")

    start_pos = 0x00600000
    end_pos   = 0x00EFFFFF
    result = calculate_sha256_range(data, start_pos, end_pos)
    print(f"The SHA256 hash of the addr 0x{start_pos:08x} to 0x{end_pos:08x} : {result}")

    start_pos = 0x00F00000
    end_pos   = 0x02EFFFFF
    result = calculate_sha256_range(data, start_pos, end_pos)
    print(f"The SHA256 hash of the addr 0x{start_pos:08x} to 0x{end_pos:08x} : {result}")

main()
