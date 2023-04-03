import socket
import threading

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def handle_client(client_socket):
    number = 1
    computerTurn = False
    while True:
        if computerTurn:
            result = str(number)
            if number % 5 == 0:
                result = str('hope :)')
            message = "my number: " + result
            client_socket.send(message.encode())
        else:
            userNumber = client_socket.recv(1024).decode().strip()
            if (number % 5 == 0 and userNumber != 'hop') or (is_integer(userNumber) and number != int(userNumber)):
                message = 'wrong number, try again\n'
                client_socket.send(message.encode())
                continue
        number += 1
        computerTurn = not computerTurn

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()
    print('Server started, listening on port 8000')
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'New client connected: {client_address}')
        t = threading.Thread(target=handle_client, args=(client_socket,))
        t.start()

if __name__ == '__main__':
    run_server()
