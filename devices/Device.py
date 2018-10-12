from net_utils.tcp.TCPClient import TCPClient
from net_utils.tcp.TCPServer import TCPServer
from net_utils.udp.UDPClient import UDPClient
from net_utils.udp.UDPServer import UDPServer


class Device:

    def __init__(self, address, name):
        self.name = name
        self.address = address
        self.tcp_client = TCPClient()
        self.udp_client = UDPClient()
        self.tcp_server = None
        self.tcp_client = None
        self.init_tcp_server()
        self.init_udp_server()
        self.devices_status = {}

    def init_tcp_server(self):
        self.tcp_server = TCPServer(*self.address, self)
        self.tcp_server.start()

    def init_udp_server(self):
        host, port = self.address
        self.udp_server = UDPServer(host, port + 1, self)
        self.udp_server.start()
