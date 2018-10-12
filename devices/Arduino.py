from interpreters.ArduinoInterpreter import ArduinoInterpreter
from net_utils.tcp.TCPClient import TCPClient
from net_utils.tcp.TCPServer import TCPServer
from net_utils.udp.UDPClient import UDPClient
from net_utils.udp.UDPServer import UDPServer
from resources.Resource import Resource
import json


class Arduino:

    def __init__(self, address, name):
        self.address = address
        self.name = name
        self.devices_status = {}
        self.resource = Resource(f"{name}-RESOURCE")
        self.tcp_client = TCPClient()
        self.udp_client = UDPClient()
        self.tcp_server = None
        self.udp_server = None
        self.init_tcp_server()
        self.init_udp_server()
        self.interpreter = ArduinoInterpreter(self)

    def init_tcp_server(self):
        self.tcp_server = TCPServer(*self.address, self)
        self.tcp_server.start()

    def init_udp_server(self):
        host, port = self.address
        self.udp_server = UDPServer(host, port + 1, self)
        self.udp_server.start()

    def set_resource_on(self):
        self.resource.set_on()

    def set_resource_off(self):
        self.set_resource_off()

    def update_device_keep_alive(self, device, timestamp):
        self.devices_status[device] = timestamp

    def add_new_device(self, new_device, timestamp):
        self.devices_status[new_device] = timestamp

    def update_devices_status_list(self, devices_list):
        self.devices_status.update(devices_list)

    def send_devices_status_list(self, destination):
        self.udp_client.send_message(destination, json.dumps(self.devices_status).encode('utf-8'))

    def call_to_action(self, message, client):
        self.interpreter.interprete_message(message, client)


if __name__ == "__main__":
    ard = Arduino(("localhost", 9087), "A01")
