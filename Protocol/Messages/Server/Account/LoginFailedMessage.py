import json
from Utils.Writer import Writer

class LoginFailedMessage(Writer):

    def __init__(self, device, player):
        super().__init__(device)
        self.device = device
        self.player = player
        self.id = 20103
        self.version = 4

    def encode(self):
        # 8 = Maintenance
        # 10  = Update Available
        # 11 = Connection Error
        self.writeByte(8) # ErrorCode
        self.writeString('') # Fingerprint
        self.writeString(None)
        self.writeString('') # Content URL
        self.writeString('') # Update URL
        self.writeString('RandomReason') # Reason
        self.writeVInt(0) # Maintenance Seconds