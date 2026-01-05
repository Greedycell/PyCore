import json
from Utils.Writer import Writer

class KeepAliveOkMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20108
        self.version = 4

    def encode(self):
        pass