import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
clients = []

server_socket.listen(1)
print("Server is listening on port 12345...")

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    clients.append(conn)
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")

            broadcast(data.decode())
        except ConnectionResetError:
            break
    clients.remove(conn)
    conn.close()

def broadcast(message):
    for client in clients:
        client.sendall(f"{message}".encode())

while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
