from WindowClass import *
import socket


class Net:
    def __init__(self):
        self.sock = 0
        self.result = 0
        self.ip = 0
        self.port = 0
        self.last_port = 0

    def single_scan(self, ip, port):
        self.ip = ip
        self.port = port
        if self.connect() == 0:
            return 0
        else:
            return 1

    def range_scan(self, ip, port, last_port):
        self.ip = ip
        self.port = int(port)
        self.last_port = int(last_port)
        for self.port in range(self.port, self.last_port):
            if self.connect() == 0:
                return 0
            else:
                return 1

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(1.5)
        return self.sock.connect_ex((self.ip, int(self.port)))
        self.sock.close()
