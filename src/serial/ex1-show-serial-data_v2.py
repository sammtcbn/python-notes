# pip uninstall serial
# pip uninstall pyserial
# pip install pyserial
# ignore upper , just use apt install -y python3-serial
import serial
import sys

# Open the serial port
try:
    print("Open serial port ...")
    ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
except:
    sys.exit ("Error opening port")

print("Serial port opened")

try:
    while True:
        # Read serial data
        if ser.in_waiting > 0:
            data = ser.readline()
            try:
                data_str = data.decode('utf-8').strip()  # Decode bytes into a string
            except UnicodeDecodeError:
                print("Error decoding data:", data)
                continue
            if data_str:
                print("Received data:", data_str)
except KeyboardInterrupt:
    # Capture keyboard interrupt signal, Ctrl+C to exit
    print("Program interrupted")
finally:
    # Close the serial port
    ser.close()

