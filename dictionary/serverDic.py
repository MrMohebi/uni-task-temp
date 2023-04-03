import random
import socket
import threading

words = {
    "a": ["abandon", "abroad"],
    "b": ["birth", "break"],
    "c": ["ceb"]
}


def handle_client(client_socket, client_address):
    print('Received connection from', client_address)

    data = client_socket.recv(1024).decode()
    if not data:
        return

    user = data
    last_char = user[-1]
    if last_char in words:
        selector = random.randint(0, len(words[last_char]) - 1)
        response = words[last_char][selector]
    else:
        response = ''

    client_socket.sendall(response.encode())

    client_socket.close()
    print('Closed connection with', client_address)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8000)
server_socket.bind(server_address)

server_socket.listen(1)
print('Server is listening on {}:{}'.format(*server_address))

while True:
    client_socket, client_address = server_socket.accept()

    t = threading.Thread(target=handle_client, args=(client_socket, client_address))
    t.start()
