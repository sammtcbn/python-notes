def get_error_message(error_code):
    error_messages = {
        0: "CPU temperature is too high",
        1: "System loading is too high",
        2: "Battery is dead"
    }
    
    return error_messages.get(error_code, "Unknown error code")

print(get_error_message(1))
print(get_error_message(2))
print(get_error_message(3))

