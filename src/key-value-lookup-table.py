import sys

# Define your data, assuming it's stored as a dictionary
data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    # Add more key-value pairs as needed
}

def search_key(key):
    if key in data:
        return data[key]
    else:
        #return "Value not found"
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide one argument as the key")
        sys.exit(1)

    key = sys.argv[1]
    result = search_key(key)
    if result == None:
        print("not found")
    else:
        print(result)
