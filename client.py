import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 7777))

    while True:
        msg = input('you>>> ')
        s.send(bytes(msg, 'utf-8'))
        body = s.recv(1024)
        print('server>>> {0}'.format(body.decode('utf-8')))
        
    s.close()