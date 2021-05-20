import socket

connection_To_Server = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')

try:
    connection_To_Server.connect((host, port))
except socket.error as e:
    print(str(e))

data = connection_To_Server.recv(1024).decode()  # receive response
print('Connection is Successful')
print(data)  # show in terminal
connection_To_Server.send(str.encode('Connection is Successful'+'\n'+'I am Client '))

connection_To_Server.close()