import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 7777))
    s.listen(1)
    clientsocket, clientaddress = s.accept()

    while True:
        body = clientsocket.recv(1024)
        print('{0}>>> {1}'.format(clientaddress[0], body.decode('utf-8')))
        msg = input('you>>> ')
        clientsocket.send(bytes(msg, 'utf-8'))

    s.close()