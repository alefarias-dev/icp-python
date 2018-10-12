import socket


class TCPClient:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_message(self, dest, message):
        self.socket.connect(dest)
        self.socket.send(message)
        self.socket.close()
