import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((self.host, self.port))

        self.nickname = None
        self.password = None

    def connect(self, nickname, password='', user=''):
        cmdNick = f"NICK {nickname}\r\n"
        cmdPass = f"PASS {password}\r\n"
        cmdUser = f"USER {nickname} {nickname} {nickname} : _{nickname}_\r\n"

        self.nickname, self.password = nickname, password

        data = [cmdNick, cmdPass, cmdUser]

        for element in data:
            self.server.send(element.encode())

    def send(self, text):
        text += "\r\n"
        self.server.send(text.encode())