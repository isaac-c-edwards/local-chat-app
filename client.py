import socket
import tkinter as tk
import threading

root = tk.Tk()
root.title("Chat Layout")


def send_message():
    message = input_line.get()
    message = message.strip()
    if message != "":
        client_socket.sendall(f"[{addr[1]}] {message}".encode())
        input_line.delete(0, tk.END)

def display_message(message):
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"{message}\n")
    chat_display.config(state="disabled")

def receive_messages():
    while True:
        data = client_socket.recv(1024).decode()
        display_message(data)
        chat_display.see(tk.END)
        

# ROW 0
chat_display = tk.Text(root, height=15, width=40)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# ROW 1, COLUMN 0:
input_line = tk.Entry(root, width=30)
input_line.grid(row=1, column=0, padx=10, pady=(0, 10)) # pady=(top, bottom)

# ROW 1, COLUMN 1
send_btn = tk.Button(root, text="Send", width=10, command=send_message)
send_btn.grid(row=1, column=1, padx=10, pady=(0, 10))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 12345))
addr = client_socket.getsockname()

server_thread = threading.Thread(target=receive_messages, daemon=True)
server_thread.start()

root.mainloop()