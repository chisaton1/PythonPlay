_author__ = 'chisaton'


#import socket module
import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Prepare a server socket
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #Establish tha connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode() #decode()でバイトからStringになる encode()はその逆
        #print(message) 確認

        filename = message.split()[1] #スペースがデフォなのでパラメータなしの場合スペースで区切る
        #print(filename) 確認
        filename = filename.split(sep='/')[1]#/で文字を分割した
        #print(filename) 確認

        with open(filename) as f: #Stringでfilenameの中身をhtmlTextへ格納
            htmlText = f.read()
            #print(htmlText) 確認


        outputdata = "HTTP/1.1 200 OK\n\n" + htmlText


        connectionSocket.sendall(outputdata.encode()) #endcode()して送る

        # #Send the content of the requested file to the client
        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i])
        connectionSocket.close()


    except IOError:
    #Send response message for file not found
    #ブラウザーにエラーメッセージを送る プリントするだけじゃダメ
        errorData = "HTTP/1.1 404 file not found\n\n" + "404 Not Found"
        connectionSocket.sendall(errorData.encode())
        #encodeして送ることでウェブサーバー上に文字が表示される。\nまではヘッダーなので表示されない

    #Close client socket
    connectionSocket.close()


#serverSocket.close()

#ウェブサーバーから呼び出すときは、127.0.0.1:12000/ファイル名.html

