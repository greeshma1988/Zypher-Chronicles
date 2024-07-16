import socket
from threading import Thread
from encryption import load_keys, decrypt_message

private_key, _ = load_keys()

def handle_client(client_socket):
    try:
        print("Client connected, waiting to receive data...")
        encrypted_message = client_socket.recv(4096)  # Increase buffer size if needed
        if not encrypted_message:
            print("No data received. Closing connection.")
            client_socket.close()
            return
        print(f"Encrypted message received: {encrypted_message}")
        decrypted_message = decrypt_message(private_key, encrypted_message)
        print(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))  # Changed port to 9999
server.listen(5)
print("Server listening on port 9999")

while True:
    try:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
    except Exception as e:
        print(f"Error accepting connections: {e}")
