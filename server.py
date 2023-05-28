import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(4096).decode()
        if not data:
            print('Client {} has disconnected'.format(client_address))
            break
        print('Received from {}: {}'.format(client_address, data))
        broadcast(data)
    client_socket.close()

def broadcast(message):
    for client, _ in clients:
        client.sendall(message.encode())

clients = []

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5002)
server_socket.bind(server_address)
server_socket.listen(5)
print('Server listening on {}:{}'.format(*server_address))

while True:
    client_socket, client_address = server_socket.accept()
    clients.append((client_socket, client_address))
    print('New connection from {}'.format(client_address))
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
