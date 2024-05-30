# pip uninstall serial
# pip uninstall pyserial
# pip install pyserial
# ignore upper , just use apt install -y python3-serial
import serial
import sys
import time

# Open the serial port
try:
    print("Open serial port ...")
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
except:
    sys.exit ("Error opening port")

print("Serial port opened")

timeout = 3  # Timeout
start_time = time.time()

#### Send data ####
ser.write(b'help\r\n')

#### Print response ####
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
        time.sleep(0.001)  # Wait for a short time to avoid busy looping
except KeyboardInterrupt:
    # Capture keyboard interrupt signal, Ctrl+C to exit
    print("Program interrupted")
finally:
    # Close the serial port
    ser.close()

print("bye")
