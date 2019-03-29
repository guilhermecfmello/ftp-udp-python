"""
  ____                              _                   _ _
 / ___|_ __ _   _ _ __   ___     __| | ___  ___   _ __ (_) | ____ _
| |  _| '__| | | | '_ \ / _ \   / _` |/ _ \/ __| | '_ \| | |/ / _` |
| |_| | |  | |_| | |_) | (_) | | (_| | (_) \__ \ | |_) | |   < (_| |
 \____|_|   \__,_| .__/ \___/   \__,_|\___/|___/ | .__/|_|_|\_\__,_|
                 |_|                             |_|
"""

#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""

from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread
from tkinter.filedialog import askopenfilename
from tkinter import *
from envelope import Pacote



def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(user.buffer_size).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


class Sender:
    # def __init__(self):
    #     self.filename = askopenfilename()
    #     print("Nome do arquivo:" + self.filename)
    #     sendFileButton.place(x=100, y=20)

    def set_ip(self, ip):
        self.ip = ip
    
    def set_port(self, port):
        self.port = port
    
    def set_file(self):
        self.filename = askopenfilename()
        self.buffer = BUFFER
        sendFileButton.place(x=100, y=100)
        # sendFileButton.tk_bisque()
    # def start(self):

   
    def sendFile(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        # sock.bind((self.ip,self.port))
        file = open(self.filename, "rb")
        data = file.read()

        n = int(len(data)/self.buffer)
        # data = dataString.encode("utf8")

        print("Tamanho: " + str(len(data)))
            # while True:
        b = str(n).encode()
        sock.sendto(b, (self.ip,self.port))
        print("Range: " + str(range(n+1)))
        print("Em bytes: " +  b.decode())
        for i in range(n+1):
            print("Entrou: " + str(i))
            packet = data[i*self.buffer:(i+1)*self.buffer]
            # packet = Pacote(self.partOfData(dataString, i), i)
            # data = self.partOfData(dataString,i)
            # while True:
            print("Enviando: " + str(packet))
            sock.sendto(packet,(self.ip,self.port))
                # print("pau tora")
                # if sock.recvfrom(self.buffer) == packet.ack:
                    # break

        # packet = Pacote("NULL".encode("utf8"),-1)

        # sock.sendto(packet,(self.ip,self.port))
            # print("dados: " + str(packet))
            # print("I: " + str(i))


        file.close()
        sock.close()


    def partOfData(self, data, i):
        return (data[(i*self.buffer):self.buffer*(i+1)])

    
def close():
    window.quit()
    
print("==============================")
print("INICIANDO TROCA DE ARQUIVOS")
print("==============================")

# user = Client("cliente", "127.0.0.1", 5502, 99, "cliente", "cliente@cliente.com")

BUFFER = 20

sender = Sender()
sender.set_ip("127.0.0.1")
sender.set_port(6061)

window = Tk()
window.title("Troca de arquivos")
window.geometry("300x300")
selectFileButton = Button(window, text="Select File", command=sender.set_file)
sendFileButton = Button(window, text="Send file", command=sender.sendFile)
closeButton = Button(window, text="Fechar", command=close)


selectFileButton.place(x=100, y=60)
closeButton.place(x=100, y=20)

window.mainloop()
# sendFileButton.place(x=100, y=20)

# sendFileButton.place_forget()


#----Now comes the sockets part----



# IP = input("Digite o ip que deseja conectar: ")
# PORT = input("Digite a porta que utilizara: ")



# print("Porta: " + user.port)
# client_socket = socket(AF_INET, SOCK_STREAM)
# client_socket.connect((user.ip, user.port))

# receive_thread = Thread(target=receive)
# receive_thread.start()