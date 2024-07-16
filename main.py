import tkinter as tk
from tkinter import messagebox
from encryption import generate_keys, save_keys, load_keys, encrypt_message, decrypt_message

private_key, public_key = generate_keys()
save_keys(private_key, public_key)

def send_message():
    message = message_entry.get()
    encrypted_message = encrypt_message(public_key, message)
    
    messagebox.showinfo("Message Sent", "Your message has been encrypted and sent.")

def receive_message():
    
    encrypted_message = b'...'  
    decrypted_message = decrypt_message(private_key, encrypted_message)
    messagebox.showinfo("Message Received", f"Decrypted message: {decrypted_message}")

root = tk.Tk()
root.title("The Zypher Chronicles")

tk.Label(root, text="Enter your message:").pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

receive_button = tk.Button(root, text="Receive", command=receive_message)
receive_button.pack()

root.mainloop()
