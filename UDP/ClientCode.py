__author__ = 'chisaton'

import socket
import time

socket.setdefaulttimeout(1)

#serverName = '127.0.0.1'
serverName = '10.229.0.128'
serverPort = 12000
countLoss = 0
countSend = 0
timeSum = 0
timeMax = 0
timeMin = 1 #1がマックス

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for num in range(0, 10):


    #message = "Ping ", num, t1
    # input('Input lowercase sentence: ')
    t1 = time.time() #メッセージを送る直前の時間を格納
    message = "ping "+ str(num)+" "+ str(t1)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    countSend += 1 #メッセージを送った回数(パーセンテージを出す際の母数)



    try: #タイムアウトするまでここで回す。タイムアウトしたら下のexceptへ(用は状況に応じた二つのパターンを列挙)
        modifiedMessage, serverAddr = clientSocket.recvfrom(1024)
        t2 = time.time() #メッセージを受け取る直前の時間を格納
        print('Modified message: ', modifiedMessage.decode())
        rtt = t2 - t1
        print(rtt)
        timeSum += rtt #10回やってかかった時間の合計(後は10で割るだけ)
        timeMax = max(rtt, timeMax)
        timeMin = min(rtt, timeMin)

    except socket.timeout: #タイムアウトした場合
        print("Request timed out")
        countLoss += 1 #パケットロスした回数


print()
print("maximum time: ",timeMax)
print("minimum time: ",timeMin)
print("average time: ",timeSum/10)
print("packet loss rate: ",countLoss/countSend)

clientSocket.close() #10回やって終了
