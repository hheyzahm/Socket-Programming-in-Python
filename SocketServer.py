import socket
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')

ServerSocket.listen(3)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        Response_from_Client = connection.recv(2048).decode('utf-8')
        reply= Response_from_Client + str(ClientNumber)
        print(reply)

        if not Response_from_Client:
            break

    connection.close()

while ThreadCount<3:
    Client, address = ServerSocket.accept()
    print('Socket is listening..')
    print('Connected to: ' + address[0] + ' : ' + str(address[1]))

    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    ClientNumber = ThreadCount
    print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()