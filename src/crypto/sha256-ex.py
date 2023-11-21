import hashlib

def calculate_sha256(filename):
    try:
        with open(filename, "rb") as file:
            file_content = file.read()
            sha256_hash = hashlib.sha256(file_content).hexdigest()
            return sha256_hash
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error calculating SHA256: {str(e)}"

def main():
    filename = "your_file_name_here"
    result = calculate_sha256(filename)
    print(f"The SHA256 hash of the file '{filename}' is: {result}")

main()
