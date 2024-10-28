# server.py
import socket

host = '0.0.0.0'  # Listen on all available interfaces
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f'Server listening on {host}:{port}')
connection, client_address = server_socket.accept()
print(f'Connected to {client_address}')

while True:
    data = connection.recv(1024).decode()
    if not data:
        break
    print(f'Received: {data}')
    connection.sendall(f'Echo: {data}'.encode())

connection.close()
server_socket.close()
