import socket
import time


class TCPClient:

    def send_message(self, dest, message):
        send = False
        while not send:
            time.sleep(0.2)
            try:
                self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket.connect(dest)
                self.socket.send(message)
                self.socket.close()
                send = True
            except:
                print('Error while sending message!')

