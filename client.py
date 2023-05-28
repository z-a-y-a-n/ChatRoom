import socket
import threading
from time import sleep

def receive_messages():
    while True:
        response = client_socket.recv(4096).decode()
        print('Received from server:', response)

def send_message():
    while True:
        message = input('Your message: ')
        client_socket.sendall(message.encode())
        sleep(2)
        if message.lower() == 'exit':
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5002)
client_socket.connect(server_address)
print('Connected to {}:{}'.format(*server_address))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

sleep(2)

send_thread = threading.Thread(target=send_message)
send_thread.start()

sleep(2)