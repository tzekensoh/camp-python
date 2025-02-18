from microbit import *
import utime

# Initialize UART with correct pins
# Connect the Fingerprint Sensor to the micro:bit
# Using the UART (TX/RX) pins:

# VCC → 3.3V (micro:bit)
# GND → GND (micro:bit)
# TX (Sensor) → RX (micro:bit, Pin 1)
# RX (Sensor) → TX (micro:bit, Pin 0)
uart.init(baudrate=57600, tx=pin0, rx=pin1)

def send_command(command):
    """Send a command to the fingerprint sensor."""
    uart.write(command)
    utime.sleep(0.1)

def read_response():
    """Read the response from the fingerprint sensor."""
    response = None
    if uart.any():
        response = uart.read()
    return response

def enroll_fingerprint(finger_id):
    """Enroll a new fingerprint with a given ID (1-127)."""
    packet_header = b'\xEF\x01\xFF\xFF\x01\x00'
    
    # Command to start enrollment
    command = packet_header + b'\x03\x01\x00\x05'
    send_command(command)
    utime.sleep(1)

    # Capture the first fingerprint image
    command = packet_header + b'\x03\x02\x00\x06'
    send_command(command)
    utime.sleep(2)

    # Convert image to template (Step 1)
    command = packet_header + b'\x03\x05\x00\x09'
    send_command(command)
    utime.sleep(1)

    # Capture the second fingerprint image
    command = packet_header + b'\x03\x02\x00\x06'
    send_command(command)
    utime.sleep(2)

    # Convert image to template (Step 2)
    command = packet_header + b'\x03\x05\x00\x09'
    send_command(command)
    utime.sleep(1)

    # Store the template in a specific ID slot
    id_high = (finger_id >> 8) & 0xFF
    id_low = finger_id & 0xFF
    store_command = packet_header + b'\x06\x06' + bytes([id_high, id_low]) + b'\x00\x0D'
    send_command(store_command)

    response = read_response()
    if response:
        display.show(Image.YES)
        print("Fingerprint Enrolled Successfully!")
    else:
        display.show(Image.NO)
        print("Failed to enroll fingerprint.")

def search_fingerprint():
    """Search for a fingerprint in the database."""
    packet_header = b'\xEF\x01\xFF\xFF\x01\x00'

    # Capture the fingerprint image
    command = packet_header + b'\x03\x02\x00\x06'
    send_command(command)
    utime.sleep(2)

    # Convert image to template
    command = packet_header + b'\x03\x05\x00\x09'
    send_command(command)
    utime.sleep(1)

    # Search for a match in the database
    command = packet_header + b'\x08\x04\x00\x07'
    send_command(command)

    response = read_response()
    if response:
        display.show(Image.HAPPY)
        print("Fingerprint Match Found!")
    else:
        display.show(Image.SAD)
        print("No Match Found.")

while True:
    if button_a.was_pressed():
        enroll_fingerprint(1)  # Enroll fingerprint with ID 1
    elif button_b.was_pressed():
        search_fingerprint()
    sleep(100)
