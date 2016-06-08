__author__ = 'chisaton'
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(True)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = serverSocket.receive(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
