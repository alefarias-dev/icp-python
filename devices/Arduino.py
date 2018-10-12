import time
from threading import Thread

from devices.Device import Device
from interpreters.ArduinoInterpreter import ArduinoInterpreter
from resources.Resource import Resource


class Arduino(Device, Thread):

    def __init__(self, address, name):
        Thread.__init__(self)
        super().__init__(address, name)
        self.resource = Resource(f"{name}-RESOURCE")
        self.interpreter = ArduinoInterpreter(self)

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
        message = {
            'action': 'deviceList',
            'list': self.devices_status
        }
        self.udp_client.send_message(destination, self.prepare_message(message))

    def keep_alive_to_all(self):
        message = {
            'action': 'keepAlive',
            'timestamp': time.time()
        }
        for device in self.devices_status.keys():
            self.udp_client.send_message(device, self.prepare_message(message))

    def call_to_action(self, message, client):
        self.interpreter.interprets_message(message, client)

    def run(self):
        while True:
            time.sleep(5)
            print(f"{self.name} sending keep-alive")
            self.keep_alive_to_all()
