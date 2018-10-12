from devices.Device import Device
from interpreters.RaspberryInterpreter import RaspberryInterpreter


class Raspberry(Device):

    def __init__(self, address, name):
        super().__init__(address, name)
        self.interpreter = RaspberryInterpreter(self)
        self.devices_status_lists = {}

    def update_devices_status_list(self, device, devices_list):
        self.devices_status_lists[device] = devices_list

    def call_to_action(self, message, client):
        pass
