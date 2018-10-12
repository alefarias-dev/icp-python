import socket
from threading import Thread


class UDPServer(Thread):

    def __init__(self, address, port, device):
        super().__init__()
        self.device = device
        self.origin = (address, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.origin)

    def receive_message(self):
        message, client = self.socket.recvfrom(1024)
        self.device.call_to_action(message, client)

    def __del__(self):
        self.socket.close()

    def run(self):
        print(f"UDPServer starts on {self.origin}")
        while True:
            self.receive_message()
