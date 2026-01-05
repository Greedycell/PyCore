from Utils.Writer import Writer
from Utils.Reader import Reader
from Logic.Player import Player

from Protocol.Messages.Server.Account.KeepAliveOkMessage import KeepAliveOkMessage

class KeepAliveMessage(Writer, Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device
        self.player = Player(device)
        self.client = device

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.client, self.player).Send()