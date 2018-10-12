import time
from threading import Thread

from devices.Arduino import Arduino
from devices.Device import Device
from interpreters.RaspberryInterpreter import RaspberryInterpreter


class Raspberry(Device, Thread):

    def __init__(self, address, name):
        Thread.__init__(self)
        super().__init__(address, name)
        self.interpreter = RaspberryInterpreter(self)
        self.devices_timestamp_lists = {}
        self.last_timestamp_devices = {}
        self.devices = []

    def update_devices_status_list(self, device, devices_list):
        self.devices_timestamp_lists[device] = devices_list

    def call_to_action(self, message, client):
        self.interpreter.interprets_message(message, client)

    def get_devices_timestamp(self):
        message = {
            'action': 'getDeviceList'
        }
        for device in self.devices:
            self.udp_client.send_message((device[0], device[1]+1), self.prepare_message(message))

    def update_last_timestamp_devices(self):
        all_devices = self.devices_timestamp_lists.keys()
        for device in all_devices:
            last_timestamp = 0
            for device_list in self.devices_timestamp_lists.items():
                device_timestamp = self.devices_timestamp_lists[device_list][device]
                last_timestamp = last_timestamp if last_timestamp > device_timestamp else device_timestamp
            self.last_timestamp_devices[device] = last_timestamp

    def update_devices_status(self):
        all_devices = self.last_timestamp_devices.items()
        time_check = round(time.time())
        for device in all_devices:
            if (time_check - self.last_timestamp_devices[device]) > 15:
                self.devices_status[device] = 0
            else:
                self.devices_status[device] = 1

    def add_new_device(self, device_address):
        self.devices.append(device_address)
        message = {
            'action': 'newDevice',
            'device': device_address
        }
        prepared_message = self.prepare_message(message)
        for device in self.devices:
            self.tcp_client.send_message(device, prepared_message)

    def run(self):
        while True:
            time.sleep(20)
            self.get_devices_timestamp()
            self.update_last_timestamp_devices()
            self.update_devices_status()
            print(self.devices_status)


if __name__ == "__main__":
    ard1 = Arduino(("localhost", 9090), "A1")
    ard1.start()
    ard2 = Arduino(("localhost", 9092), "A2")
    ard2.start()

    rasp = Raspberry(("localhost", 9098), "RASP-MASTER")
    rasp.add_new_device(("localhost", 9090))
    rasp.add_new_device(("localhost", 9092))
    rasp.start()

