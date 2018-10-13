import sys
import json

sys.path.append('..')

from net_utils.tcp.TCPClient import TCPClient
from net_utils.tcp.TCPServer import TCPServer
from net_utils.udp.UDPClient import UDPClient
from net_utils.udp.UDPServer import UDPServer


class Device:

    def __init__(self, address, name):
        self.name = name
        self.address = address
        host, port = self.address
        self.tcp_client = TCPClient()
        self.udp_client = UDPClient()
        self.tcp_server = TCPServer(*self.address, self)
        self.udp_server = UDPServer(host, port + 1, self)
        self.tcp_server.start()
        self.udp_server.start()
        self.devices_status = {}

    def prepare_message(self, message_dict):
        return json.dumps(message_dict).encode("utf-8")

    def __del__(self):
        self.tcp_client.socket.close()
        self.udp_client.socket.close()
        self.tcp_server.socket.close()
        self.udp_server.socket.close()
