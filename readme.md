# Simple Chat App

This project is a basic TCP chat application built in Python. It includes:

- A threaded chat server (`server.py`) that accepts multiple clients and broadcasts messages.
- A desktop chat client (`client.py`) built with Tkinter.

The app currently runs on `localhost` and is intended for local testing and learning socket programming concepts.

## Instructions for Build and Use

No build step is required.

1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Start the server.
4. Open one or more additional terminals and start clients.


### How to Use

1. Start the server first.
2. Launch at least two client windows.
3. Type a message in one client and click **Send**.
4. The server broadcasts that message to all connected clients.

Each outgoing message is prefixed with the client socket port in this format: `[port] message`.

## Development Environment

To recreate this environment, use:

- Python 3.x
- Python standard library modules only:
	- `socket`
	- `threading`
	- `tkinter`
- Any code editor or IDE (VS Code recommended)

## Useful Websites to Learn More

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Python threading documentation](https://docs.python.org/3/library/threading.html)
- [Tkinter documentation](https://docs.python.org/3/library/tkinter.html)

## Future Work

- [ ] Add usernames instead of displaying socket port numbers.
- [ ] Add input validation and error handling for network failures.
- [ ] Support running over LAN by configuring host/IP and port settings.
