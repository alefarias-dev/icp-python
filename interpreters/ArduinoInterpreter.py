import json
import time
from devices.Arduino import Arduino


class ArduinoInterpreter:

    def __init__(self, device):
        self.device = device

    def interprete_message(self, msg, client=("localhost", 9087)):
        message = json.loads(msg)
        action = message['action']

        # A1 - From Arduino
        if action == 'keepAlive':
            timestamp = message['timestamp']
            self.device.update_device_keep_alive(client, timestamp)
            return

        # R1 - From Raspberry
        if action == 'newDevice':
            new_device = message['device']
            timestamp = round(time.time())
            self.device.add_new_device(new_device, timestamp)
            return

        # R2
        if action == 'changeResourceStatus':
            status = message['status']
            self.device.resource.set_on() if status == 1 else self.device.resource.set_off()
            return

        # R4
        if action == 'getDeviceList':
            self.device.send_devices_status_list(client)
            return

        # R5 - From Raspberry
        if action == 'updateDeviceList':
            devices_status = dict(message['list'])
            self.device.update_devices_status_list(devices_status)
            return


if __name__ == "__main__":
    ard = Arduino(("localhost", 9087), "AU01")
    interpreter = ArduinoInterpreter(ard)
    message = {'action': 'keepAlive', 'timestamp': 123144123}
    message2 = {'action': 'newDevice', 'device': 'localhost:9090'}
    message3 = {
        'action': 'updateDeviceList',
        'list': {
            'localhost:9087': 123123213,
            'localhost:9089': 433242233,
            'localhost:9091': 132134411,
            'localhost:9090': round(time.time()) + 2
        }
    }
    message4 = {
        'action': 'changeResourceStatus',
        'status': 1
    }
    interpreter.interprete_message(json.dumps(message))
    print(ard.devices_status)
    interpreter.interprete_message(json.dumps(message2))
    print(ard.devices_status)
    interpreter.interprete_message(json.dumps(message3))
    print(ard.devices_status)
    interpreter.interprete_message(json.dumps(message4))
    print(ard.resource)
