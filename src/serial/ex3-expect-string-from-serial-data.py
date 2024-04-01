# pip uninstall serial
# pip uninstall pyserial
# pip install pyserial
import serial
import time

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Modify according to your serial port and baud rate

expected_string = "booting is done"
timeout = 300  # Timeout in seconds (5 minutes)
no_data_timeout = 30  # Timeout in seconds to exit if no data received
start_time = time.time()

try:
    while (time.time() - start_time) < timeout:
        # Check overall timeout
        data = ser.readline()  # Read a line of data
        try:
            data_str = data.decode('utf-8').strip()  # Decode bytes into a string
        except UnicodeDecodeError:
            print("Error decoding data:", data)
            continue
        if data_str:
            print("Received data:", data_str)
            if expected_string in data_str:
                print("Found '", expected_string, "'. Exiting the loop.")
                break
            start_time = time.time()  # Reset the start time since data is received
        elif (time.time() - start_time) > no_data_timeout:
            print("No data received for", no_data_timeout, "seconds. Exiting the loop.")
            break
        time.sleep(0.1)  # Wait for a short time to avoid busy looping
    else:
        print("Timeout: '", expected_string, "' not received within 5 minutes.")
except KeyboardInterrupt:
    # Capture keyboard interrupt signal, Ctrl+C to exit
    print("Program interrupted")
finally:
    # Close the serial port
    ser.close()

