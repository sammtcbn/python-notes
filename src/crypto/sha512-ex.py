import hashlib

def calculate_sha512(filename):
    try:
        with open(filename, "rb") as file:
            file_content = file.read()
            shahash = hashlib.sha512(file_content).hexdigest()
            return shahash
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error calculating SHA512: {str(e)}"

def main():
    filename = "your_file_name_here"
    result = calculate_sha512(filename)
    print(f"The SHA512 hash of the file '{filename}' is: {result}")

main()
