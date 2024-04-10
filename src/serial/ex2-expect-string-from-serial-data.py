# pip uninstall serial
# pip uninstall pyserial
# pip install pyserial
# ignore upper , just use apt install -y python3-serial
import serial
import time
import sys

# Open the serial port
try:
    print("Open serial port ...")
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Modify according to your serial port and baud rate
except:
    sys.exit ("Error opening port")

print("Serial port opened")

expected_string = "booting is done"
timeout = 300  # Timeout in seconds (5 minutes)
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
        time.sleep(0.1)  # Wait for a short time to avoid busy looping
    else:
        print("Timeout: '", expected_string, "' not received within 5 minutes.")
except KeyboardInterrupt:
    # Capture keyboard interrupt signal, Ctrl+C to exit
    print("Program interrupted")
finally:
    # Close the serial port
    ser.close()

