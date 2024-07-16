import socket
from encryption import load_keys, encrypt_message

_, public_key = load_keys()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("Connecting to server...")
    client.connect(('127.0.0.1', 9999))  # Connect to server on port 9999
    print("Connected to server. Sending message...")
    message = "Hello, this is a test message."
    encrypted_message = encrypt_message(public_key, message)
    client.send(encrypted_message)
    print("Encrypted message sent.")
except Exception as e:
    print(f"Error connecting or sending data: {e}")
finally:
    client.close()
    print("Client socket closed.")
