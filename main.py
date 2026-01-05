import json
import socket
from threading import Thread
from Protocol.MessageFactory import *
from Logic.Device import Device

config = json.load(open("config.json", "r"))
server_address = ("0.0.0.0", config["Port"])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

class ClientSocket(Thread):
    def __init__(self, client, address):
        super().__init__(daemon=True)
        self.client = client
        self.address = address
        self.device = Device(client)

    def recvall(self, size):
        data = b""
        while len(data) < size:
            chunk = self.client.recv(size - len(data))
            if not chunk:
                raise EOFError
            data += chunk
        return data

    def run(self):
        print("[*] >> A connection has appeared!", self.address)
        try:
            while True:
                header = self.client.recv(7)
                if not header:
                    break
                packetid = int.from_bytes(header[:2], "big")
                length   = int.from_bytes(header[2:5], "big")
                version  = int.from_bytes(header[5:], "big")
                payload = self.recvall(length)
                if packetid in MessageFactory:
                    msg = MessageFactory[packetid](payload, self.device)
                    msg.decode()
                    msg.process()
                else:
                    print("[*] >> Unhandled packet:", packetid)

        except Exception as e:
            print("[*] >> Client error:", e)

        finally:
            self.client.close()

class StartServer:
    def run(self):
        sock.bind(server_address)
        # listen for connections
        sock.listen()
        print("[SERVER] >> Listening on 0.0.0.0:{}".format(config['Port']))

        while True:
            client, addr = sock.accept()
            ClientSocket(client, addr).start()

if __name__ == "__main__":
    StartServer().run()