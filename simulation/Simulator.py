import sys
import json

sys.path.append('..')

from threading import Thread
from devices.Arduino import Arduino
from devices.Raspberry import Raspberry


class ICPSimulator(Thread):

    def __init__(self):
        super().__init__()
        self.configuration = {}
        self.devices = []
        self.devices_address = []
        self.raspberry = self.create_raspberry()
        self.load_config()

    def load_config(self):
        with open('config', 'r') as config_file:
            content = config_file.read()
            self.configuration = json.loads(content)

    def create_devices(self):
        print(self.configuration)
        devices = self.configuration['devices']
        for device in devices.keys():
            host = devices[device]['host']
            port = devices[device]['port']
            name = devices[device]['name']
            failure_risk = devices[device]['failure_risk']
            address = (host, int(port))
            self.devices.append(Arduino(address, name, failure_risk))
            self.devices_address.append(address)

    def create_raspberry(self):
        return Raspberry(("localhost", 20001), "RASPBERRY")

    def associate_devices(self):
        for device_address in self.devices_address:
            self.raspberry.add_new_device(device_address)

    def start_devices(self):
        for device in self.devices:
            print(f"{device} started")
            device.start()

    def start_raspberry(self):
        self.raspberry.start()
        self.raspberry.join()

    def start_simulation(self):
        self.create_devices()
        self.start_devices()
        self.associate_devices()
        self.start_raspberry()


if __name__ == "__main__":
    simulator = ICPSimulator()
    simulator.start_simulation()
