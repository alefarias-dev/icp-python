from threading import Thread

from devices.Device import Device
from interpreters.RaspberryInterpreter import RaspberryInterpreter


class Raspberry(Device, Thread):

    def __init__(self, address, name):
        Thread.__init__(self)
        super().__init__(address, name)
        self.interpreter = RaspberryInterpreter(self)
        self.devices_status_lists = {}

    def update_devices_status_list(self, device, devices_list):
        self.devices_status_lists[device] = devices_list

    def call_to_action(self, message, client):
        self.interpreter.interprets_message(message, client)

    def run(self):
        pass
