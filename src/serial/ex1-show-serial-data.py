# pip uninstall serial
# pip uninstall pyserial
# pip install pyserial
import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 115200)

try:
    while True:
        # Read serial data
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print("Received data:", data)
except KeyboardInterrupt:
    # Capture keyboard interrupt signal, Ctrl+C to exit
    print("Program interrupted")
finally:
    # Close the serial port
    ser.close()

