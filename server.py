import socket
import asyncio


class Server:
    def __init__(self, host:str, port:str):
        self.host = host
        self.port = port

        self.server_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def close(self):
        self.server_client.close()
        socket.close()

    """
    METHODE serverConnection()
        but: Se connecte au serveur self.host:selfport
        args:
            None
        returns:
            None
    """
    def serverConnection(self):
        print(f"[+] Connexion au serveur -> {self.host}:{self.port}")
        self.server_client.connect((self.host, self.port))

    """
    METHODE serverAuthentification(nickname, password)
        but: Authentification nom et mot_de_passe
        args:
            nickname: str
            password: str
        returns:
            None
    """
    def serverAuthentification(self, nickname, password=""):
        cmdNICK = f"NICK {nickname}\r\n"
        cmdPASS = f"PASS {nickname}\r\n"
        cmdUSER = f"USER {nickname} {nickname} {nickname} : _{nickname}_\r\n"

        dataCONNECTION = [cmdPASS, cmdNICK, cmdUSER]
        for data in dataCONNECTION:
            self.server_client.send(data.encode())

        temp = ""
        for i in password:
            temp += "*"

        print(
            "[+] Authentification: \n",
            f"\tNom de l'utilisateur: {nickname}\n",
            f"\tMot de passe: {temp}"
        )

    """
    METHODE sendMessage(message)
        but: Envoie du message sur le serveur
        args:
            massage: str
        return:
            None
    """
    def sendMessage(self, message):
        msg = f"{message}\r\n"
        self.server_client.send(msg.encode())

    """
    METHODE messageListener()
        but: Fonction d'écoute du serveur
        args:
            None
        return:
            None
    """
    def messageListener(self):
        text = self.server_client.recv(2040)
        print(text.decode("UTF-8"))

