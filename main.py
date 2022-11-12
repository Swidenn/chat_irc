from client import *

def main():
    application = QApplication([])
    connection_window = ConnectionGui()

    application.exec_()

if __name__ == '__main__':
    main()
