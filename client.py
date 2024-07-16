import socket
from encryption import load_keys, encrypt_message

_, public_key = load_keys()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

message = "Hello, this is a test message."
encrypted_message = encrypt_message(public_key, message)
client.send(encrypted_message)
