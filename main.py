from server import Server
from client import Client
import threading


SERVER = Server("open.ircnet.net", 6667)
CLIENT = Client("Freddy")

SERVER.serverConnection()
SERVER.serverAuthentification("Freddy", "Dude")

def SEND_MESSAGE():
    while True:
        _message = CLIENT.getMessage()
        SERVER.sendMessage(_message)

def LISTENER():
    while True:
        SERVER.messageListener()

_envoie = threading.Thread(target=SEND_MESSAGE)
_recoie = threading.Thread(target=LISTENER)

_envoie.start()
_recoie.start()

#_envoie.join()
_recoie.join()

SERVER.close()
