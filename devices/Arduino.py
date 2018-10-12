from net_utils.tcp.TCPServer import TCPServer


class Arduino:

    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.tcp_server = TCPServer(*address, self)
        self.tcp_server.start()

    def call_to_action(self, message):
        print(f"Received message to call to action: {message}")


if __name__ == "__main__":
    ard = Arduino(("localhost", 9087), "AUNO-01")
