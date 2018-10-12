import json


class RaspberryInterpreter:

    def __init__(self, device):
        self.device = device

    def interprete_message(self, msg, client):
        message = json.loads(msg)
        action = message['action']


if __name__ == "__main__":
    pass
