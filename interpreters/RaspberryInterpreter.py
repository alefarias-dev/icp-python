import json


class RaspberryInterpreter:

    def __init__(self, device):
        self.device = device

    def interprets_message(self, msg, client):
        protocol_message = json.loads(msg.decode('utf-8'))
        action = protocol_message['action']

        if action == 'deviceList':
            devices_list = dict(protocol_message['list'])
            origin = protocol_message['origin']
            self.device.update_devices_status_list(tuple(origin), devices_list)
