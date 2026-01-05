import json
from Utils.Writer import Writer

class ServerHelloMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20100
        self.version = 1

    def encode(self):
        self.writeInt(24)
        self.writeBytes(urandom(24))  # SessionKey