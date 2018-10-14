import json
import sys
import time

sys.path.append('..')

from threading import Thread
from devices.Arduino import Arduino
from devices.Raspberry import Raspberry


class ICPSimulator(Thread):

    def __init__(self, interface_simulator):
        super().__init__()
        self.interface_simulator = interface_simulator
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

    def run(self):
        self.create_devices()
        self.start_devices()
        self.associate_devices()
        self.start_raspberry()
        if self.interface_simulator:
            while True:
                time.sleep(1.3)
                self.update_interface()

    def update_interface(self):
        self.interface_simulator.update_log_text()
        self.interface_simulator.update_devices_status()


if __name__ == "__main__":
    simulator = ICPSimulator(None)
    simulator.start()
    simulator.join()
