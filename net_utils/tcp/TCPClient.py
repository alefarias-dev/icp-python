import socket


class TCPClient:

    def send_message(self, dest, message):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(dest)
        self.socket.send(message)
        self.socket.close()
