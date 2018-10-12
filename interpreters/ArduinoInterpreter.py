import json
import time


class ArduinoInterpreter:

    def __init__(self, device):
        self.device = device

    def interprets_message(self, msg, client=("localhost", 9087)):
        protocol_message = json.loads(msg.decode('utf-8'))
        action = protocol_message['action']

        # A1 - From Arduino
        if action == 'keepAlive':
            timestamp = protocol_message['timestamp']
            self.device.update_device_keep_alive(client, timestamp)
            return

        # R1 - From Raspberry
        if action == 'newDevice':
            new_device = protocol_message['device']
            timestamp = round(time.time())
            self.device.add_new_device(new_device, timestamp)
            return

        # R2
        if action == 'changeResourceStatus':
            status = protocol_message['status']
            self.device.resource.set_on() if status == 1 else self.device.resource.set_off()
            return

        # R4
        if action == 'getDeviceList':
            self.device.send_devices_status_list(client)
            return

        # R5 - From Raspberry
        if action == 'updateDeviceList':
            devices_status = dict(protocol_message['list'])
            self.device.update_devices_status_list(devices_status)
            return
