import hashlib

def calculate_md5(file_path):
    md5_hash = hashlib.md5()
    try:
        with open(file_path, "rb") as file:
            # Read and update hash string value in blocks of 4K
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error calculating MD5: {str(e)}"

def main():
    file_path = "your_file_name_here"
    md5_checksum = calculate_md5(file_path)
    print(f"MD5 checksum of '{file_path}': {md5_checksum}")

main()
