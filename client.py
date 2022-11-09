from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from server import Server
from utils import formattage
import time


TEXT_RECIVED = ""
SERVER = None

class ConnectionGui(QMainWindow):
    def __init__(self):
        super(ConnectionGui, self).__init__()
        uic.loadUi("GUI/connection.ui", self)

        self.pushButton.clicked.connect(self.on_clicked)

        self.server = None
        self.main_gui = None

        self.show()

    def on_clicked(self):
        global SERVER

        self.server = Server(self.lineEdit_3.text(), int(self.lineEdit_4.text()))
        self.server.connect(self.lineEdit.text(), self.lineEdit_2.text())

        SERVER = self.server

        self.main_gui = MainGui()
        self.close()

class MainGui(QMainWindow):
    def __init__(self):
        super(MainGui, self).__init__()
        uic.loadUi("GUI/main.ui", self)

        self.pushButton.clicked.connect(lambda: self.sendMessage(self.lineEdit.text()))
        self.lineEdit.returnPressed.connect(lambda: self.sendMessage(self.lineEdit.text()))

        self.nickname = SERVER.nickname

        self.text = ""

        self.recivedMessage()
        self.show()

    def sendMessage(self, msg):
        if msg != '':
            SERVER.send(msg)

            text = f"[{self.nickname}]: {msg}\r\n"

            self.plainTextEdit.appendPlainText(text)
            self.lineEdit.clear()

    def recivedMessage(self):
        self.listener_signal_thread = ListenerSignalThread()
        self.listener_signal_thread.info.connect(self.printRecivedMessage)
        self.listener_signal_thread.start()

    def printRecivedMessage(self):
        text = f"{formattage(TEXT_RECIVED)}"
        self.plainTextEdit.appendPlainText(text)

class ListenerSignalThread(QThread):
    info = pyqtSignal(str)
    fini = pyqtSignal(bool, list)

    def __init__(self, parent=None):
        super(ListenerSignalThread, self).__init__(parent)

    def run(self):
        global TEXT_RECIVED

        while True:
            text = SERVER.server.recv(2040)
            TEXT_RECIVED = text.decode("UTF-8")

            if TEXT_RECIVED != "":
                self.info.emit(TEXT_RECIVED)

