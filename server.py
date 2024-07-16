import socket
from threading import Thread
from encryption import load_keys, decrypt_message

private_key, _ = load_keys()

def handle_client(client_socket):
    encrypted_message = client_socket.recv(1024)
    decrypted_message = decrypt_message(private_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)
print("Server listening on port 9999")

while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    client_handler = Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

