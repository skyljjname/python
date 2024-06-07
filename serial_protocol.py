
import serial
import time

def read_serial(port, baudrate, timeout=1):
    """
    Function to read data from a serial port and print it.
    
    Parameters:
    port (str): The port to which the serial device is connected (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux).
    baudrate (int): The baud rate for the serial communication.
    timeout (int): The read timeout value in seconds.
    """
    try:
        # Open the serial port
        ser = serial.Serial(port, baudrate, timeout=timeout)
        print(f"Opened serial port {port} with baudrate {baudrate}")

        while True:
            if ser.in_waiting > 0:
                # Read data from the serial port
                data = ser.readline().decode('utf-8').rstrip()
                print(f"Received: {data}")
            else:
                # No data, sleep for a while to avoid busy-waiting
                time.sleep(0.1)

    except serial.SerialException as e:
        print(f"Error opening serial port {port}: {e}")
    except KeyboardInterrupt:
        print("Program interrupted by user.")
    finally:
        # Ensure the serial port is closed
        if ser.is_open:
            ser.close()
            print(f"Closed serial port {port}")

if __name__ == "__main__":
    # Replace 'COM3' with your serial port name and 9600 with your baud rate
    read_serial(port='COM31', baudrate=9600)
