import socket


class UDPClient:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, address, message):
        self.socket.sendto(message, address)
