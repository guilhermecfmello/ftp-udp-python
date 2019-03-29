"""
  ____                              _                   _ _
 / ___|_ __ _   _ _ __   ___     __| | ___  ___   _ __ (_) | ____ _
| |  _| '__| | | | '_ \ / _ \   / _` |/ _ \/ __| | '_ \| | |/ / _` |
| |_| | |  | |_| | |_) | (_) | | (_| | (_) \__ \ | |_) | |   < (_| |
 \____|_|   \__,_| .__/ \___/   \__,_|\___/|___/ | .__/|_|_|\_\__,_|
                 |_|                             |_|
"""

#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread
from client import Client
from tkinter.filedialog import askdirectory
from tkinter import *
from envelope import Pacote




# def broadcastFile(file):
        
#         for sock in clientsFile:
#                 sock.send(bytes())


class Receiver():

        def __init__(self, ip, port):
                self.ip = ip
                self.port = port

        def setDirectory(self):
                self.dir = askdirectory()
                receiveButton.place(x=100,y=100)
                # print("Dir: " + self.dir)

        def receiveFile(self):
                sock = socket(AF_INET, SOCK_DGRAM)
                sock.bind((self.ip,self.port))
                print("Inicio recebimento")
                data, addr = sock.recvfrom(BUFFER)
                # n = int.from_bytes(data, byteorder='big')
                n = int(data.decode())
                # while True:
                print(str(range(n)))
                dataWrite = bytes(0)
                for i in range(n+1):
                        # print("Teste")
                        data, addr = sock.recvfrom(BUFFER)
                        print("Recebido: " + str(data))
                        # packet = Pacote(data[0:BUFFER],data[BUFFER:BUFFER+4])
                        # print("Tipo pacote: " + type(packet))
                        # if packet.ack == -1:
                        #         break
                        dataWrite = dataWrite + data
                        # sock.sendto(ack(self.ip,self.port))
                print("Fim recebimento")
                print("Gravando em "+ self.dir)
                file = open(self.dir+"/recebido2.txt","wb")
                file.write(dataWrite)
                file.close()
                sock.close()


def close():
        window.quit()

receiver = Receiver("127.0.0.1", 6061)

BUFFER = 20

window = Tk()
window.title("Sender")
window.geometry("300x300")
selectFileButton = Button(window, text="Selecionar diretorio", command=receiver.setDirectory)
closeButton = Button(window, text="Fechar", command=close)
receiveButton = Button(window, text="Iniciar FTP", command=receiver.receiveFile)

selectFileButton.place(x=100, y=60)
closeButton.place(x=100, y=20)
# port = input("Digite a porta que utilizara: ")



window.mainloop()

user = Client("server", "127.0.0.1", 5502, 99, "estudante", "uel.br")


BUFFER_FILE = 20

SERVER = socket(AF_INET, SOCK_DGRAM)
SERVER.bind((user.ip, int(user.port)))

SERVER.close()
