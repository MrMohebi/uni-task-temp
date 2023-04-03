import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8000)
client_socket.connect(server_address)

# Prompt the user for input and send it to the server
while True:
    user_input = input('Enter a word: ')
    if user_input == 'exit':
        break
    client_socket.sendall(user_input.encode())

    # Receive and print the response from the server
    response = client_socket.recv(1024).decode()
    print(response)

# Close the socket
client_socket.close()