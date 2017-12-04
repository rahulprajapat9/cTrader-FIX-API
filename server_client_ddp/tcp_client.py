import socket

def Main():
    host = 'tcp://192.168.0.115'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = raw_input("->")
    while message!='q':
        s.send(message)
        data = s.recv(1024)
        print 'Received from server: ', str(data)

        message = raw_input("->")

    s.close()




if __name__ == '__main__':
    Main()



