import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket successfully created')
except socket.error as err:
    print('socket creation failed because'+str(err))

port=10000
host=input('your ip?')
s.bind((host,port))
print(f'Socket is binded to port {port}')
s.listen(5)
print('Socket is listening')


while True:
    connection,address=s.accept()
    print('Got connection from '+address[0])
    connection.send('The dark side has chosen you huhuh'.encode())

    break
