# client.py
import socket

host = 'your_rpi_ip_address'  # Replace with your Raspberry Pi's IP
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = input("Enter message to send: ")
client_socket.sendall(message.encode())

data = client_socket.recv(1024).decode()
print(f'Received from server: {data}')

client_socket.close()
