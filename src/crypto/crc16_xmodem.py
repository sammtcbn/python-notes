import sys

def calculate_crc16_xmodem(data):
    poly = 0x1021
    crc = 0x0000

    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
        crc &= 0xFFFF  # Ensure CRC remains a 16-bit value

    return crc

def main():
    if len(sys.argv) != 2:
        print("Usage: python crc16_xmodem.py <data>")
        sys.exit(1)

    input_data = sys.argv[1]
    # Convert input string to bytes
    data_bytes = bytes.fromhex(input_data)

    # Calculate CRC-16-XMODEM
    crc_result = calculate_crc16_xmodem(data_bytes)

    # Print the result as hexadecimal
    print(f"CRC-16-XMODEM result: 0x{crc_result:04X}")

if __name__ == "__main__":
    main()

'''
Result:
$ python3 crc16_xmodem.py C61AC0
CRC-16-XMODEM result: 0xA1A3

$ python3 crc16_xmodem.py C5A55A
CRC-16-XMODEM result: 0xD433

$ python3 crc16_xmodem.py c203aabbcc
CRC-16-XMODEM result: 0x4C8D
'''
