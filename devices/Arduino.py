from net_utils.tcp.TCPClient import TCPClient
from net_utils.tcp.TCPServer import TCPServer
from net_utils.udp.UDPClient import UDPClient
from net_utils.udp.UDPServer import UDPServer
from resources.Resource import Resource


class Arduino:

    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.resource = Resource(f"{name}-RESOURCE")
        self.tcp_client = TCPClient()
        self.udp_client = UDPClient()
        self.tcp_server = None
        self.udp_server = None
        self.init_tcp_server()
        self.init_udp_server()

    def init_tcp_server(self):
        self.tcp_server = TCPServer(*self.address, self)
        self.tcp_server.start()

    def init_udp_server(self):
        host, port = self.address
        self.udp_server = UDPServer(host, port + 1, self)

    def set_resource_on(self):
        self.resource.set_on()

    def set_resource_off(self):
        self.set_resource_off()

    def call_to_action(self, message):
        print(f"Received message to call to action: {message}")


if __name__ == "__main__":
    ard = Arduino(("localhost", 9087), "A01")
