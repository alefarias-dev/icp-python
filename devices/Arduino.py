import json
from devices.Device import Device
from interpreters.ArduinoInterpreter import ArduinoInterpreter
from resources.Resource import Resource


class Arduino(Device):

    def __init__(self, address, name):
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
        self.udp_client.send_message(destination, json.dumps(self.devices_status).encode('utf-8'))

    def call_to_action(self, message, client):
        # self.interpreter.interprete_message(message, client)
        pass


if __name__ == "__main__":
    ard = Arduino(("localhost", 9087), "A01")
