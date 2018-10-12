import random
import time
from threading import Thread

from devices.Device import Device
from interpreters.ArduinoInterpreter import ArduinoInterpreter
from resources.Resource import Resource


class Arduino(Device, Thread):

    def __init__(self, address, name, failure_prob):
        Thread.__init__(self)
        super().__init__(address, name)
        self.resource = Resource(f"{name}-RESOURCE")
        self.interpreter = ArduinoInterpreter(self)
        self.failure_prob = failure_prob

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
            'origin': self.address,
            'list': self.parse_device_status()
        }
        self.tcp_client.send_message(destination, self.prepare_message(message))

    def parse_device_status(self):
        parsed = {}
        for device in self.devices_status.keys():
            host, port = device
            key = ":".join([host, str(port)])
            parsed[key] = self.devices_status[device]
        return parsed

    def keep_alive_to_all(self):
        message = {
            'action': 'keepAlive',
            'device': self.address,
            'timestamp': round(time.time())
        }
        device_status_copy = self.devices_status.copy()
        for device in device_status_copy:
            self.udp_client.send_message((device[0], device[1]+1), self.prepare_message(message))

    def call_to_action(self, message, client):
        self.interpreter.interprets_message(message, client)

    def run(self):
        while True:
            time.sleep(.5)
            self.keep_alive_to_all()
            # print(f"{self.name}: {self.devices_status}")
            if random.random() < self.failure_prob:
                print(f"{self.name}: I failed!")
                time.sleep(10)
