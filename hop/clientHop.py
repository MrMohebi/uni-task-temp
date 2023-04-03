import socket


def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8558))
        while True:
            user_input = input('ur turn: ')
            s.send(user_input.encode())

            message = s.recv(1024).decode().strip()
            if not message:
                break
            print(message)


if __name__ == '__main__':
    run_client()
