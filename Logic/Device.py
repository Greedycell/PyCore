import traceback

from Protocol.MessageFactory import *

class Device:
    def __init__(self, socket=None):
        self.socket = socket

    def SendData(self, ID, data, version=None):
        packetID   = ID.to_bytes(2, 'big')
        if version:
            packetVersion = version.to_bytes(2, 'big')
        else:
            packetVersion = (0).to_bytes(2, 'big')
        if self.socket is None:
            self.transport.write(packetID + len(data).to_bytes(3, 'big') + packetVersion + data)
        else:
            self.socket.send(packetID + len(data).to_bytes(3, 'big') + packetVersion + data)
        print('[*] Received packet:', ID)

    def processPacket(self, packetID, payload):
        print('[*] >> Handled packet:', packetid)
        try:
            if packetID in MessageFactory:
                Message = MessageFactory[packetID](payload, self)
                Message.decode()
                Message.process()
            else:
                print('[*] >> Unhandled packet:', packetid)
        except:
            print('[*] >> Error while decrypting packet:', packetid)

    def close(self):
        if self.socket:
            try:
                self.socket.shutdown(2)  # stop both send and receive
            except OSError:
                pass  # socket may already be closed
            finally:
                try:
                    self.socket.close()
                    print("[*] Client disconnected")
                except Exception as e:
                    print(f"[*] Error closing socket: {e}")
            self.socket = None
        else:
            print("[*] Socket already closed or not set")