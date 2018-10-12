import socket
from threading import Thread


class TCPServer(Thread):

    def __init__(self, address, port, device):
        super().__init__()
        self.device = device
        self.address = address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.origin = (address, port)
        self.socket.bind(self.origin)
        self.socket.listen(1)

    def receive_message(self):
        connection, client = self.socket.accept()
        message = connection.recv(1024)
        connection.close()
        self.device.call_to_action((message.decode("utf-8"), client))

    def __del__(self):
        self.socket.close()

    def run(self):
        print(f"TCPServer starts on {self.origin}")
        while True:
            self.receive_message()
