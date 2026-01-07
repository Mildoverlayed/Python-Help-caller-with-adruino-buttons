import tkinter
import json
import serial
from typing import List, Tuple
import threading
import time

def update_needshelp(data_index: int, button: tkinter.Button) -> None:
    # Update the data
    data[data_index]['NEEDSHELP'] = 0
    # Save back to JSON
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    # Refresh the GUI after update
    refresh_gui()

def refresh_gui():
    global data, frame
    # Reload data
    with open('data.json', 'r') as f:
        data = json.load(f)
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()
    # Recreate buttons
    for i, item in enumerate(data):
        if item['NEEDSHELP'] == 1:
            button = tkinter.Button(frame, text=f"Name: {item['NAME']}")
            button.config(command=lambda idx=i, btn=button: update_needshelp(idx, btn))
            button.pack(anchor='w')

def read_serial_data(ser: serial.Serial) -> tuple[bool, bytes]:
    """simple call to read the incoming traffic of a serial interface 4 bytes at a time

    Args:
        ser (serial.Serial): serial interface to read form

    Returns:
        tuple[bool, bytes]: returns true if data was recived and what that data was
    """
    if ser.in_waiting > 0:
        data_bytes = ser.read(4)
        return True, data_bytes
    else:
        return False, b''

def serial_reader_thread():
    """Background thread to read serial data and update data.json"""
    global data
    while True:
        for _, ser in serial_ports:
            success, received_bytes = read_serial_data(ser)
            if success:
                if len(received_bytes) == 4:
                    if (received_bytes[0] == 0x0f and received_bytes[3] == 0xf0):
                        print(f"Data received from ID: {received_bytes[1]:02X} with INDEX: {received_bytes[2]:02X}")
                        for item in data:
                            if item['ID'] == received_bytes[1] and item['INDEX'] == received_bytes[2]:
                                print(f"Item found: {item} set to 1")
                                item["NEEDSHELP"] = 1
                                # Sync to JSON
                                with open("data.json", "w") as file:
                                    json.dump(data, file, indent=4)
        time.sleep(0.1)  # Small delay to avoid busy-waiting

m = tkinter.Tk()

# Load data from data.json
with open('data.json', 'r') as f:
    data = json.load(f)

# Load configurations for serial ports
with open('config.json', 'r') as file:  
    configs = json.load(file)
serial_ports: List[Tuple[str, serial.Serial]] = []
for config in configs:
    try:
        ser = serial.Serial(config['port'], config['baudrate'], timeout=config['timeout'])
        serial_ports.append((config['ID'], ser))
        print(f"Opened port for ID: {config['ID']}")
    except serial.SerialException as e:
        print(f"Failed to open port for ID {config['ID']}: {e}")

# Create a frame for the data display
frame = tkinter.Frame(m)
frame.pack(pady=10)

# Initial GUI setup
refresh_gui()

# Start serial reader in a background thread
threading.Thread(target=serial_reader_thread, daemon=True).start()

# Auto-refresh GUI every 1 second
def auto_refresh():
    refresh_gui()
    m.after(1000, auto_refresh)
auto_refresh()

m.mainloop()