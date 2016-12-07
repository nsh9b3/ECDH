#file for two party communication

import socket
import time


def sendInfo(stringToSend,tcp_ip,tcp_port):
    print("Sending")
    #buffer shouldn't need to be this big
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    s.send(bytes(stringToSend,'UTF-8'))
    data = s.recv(BUFFER_SIZE)
    s.close()
    
def recInfo(point,myIpAddress,myPort):
    print("Recieving")
    #buffer shouldn't need to be this big
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((myIpAddress, myPort))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)
    data = ""
    while 1:
        rec = conn.recv(BUFFER_SIZE).decode('UTF-8')
        if not rec: break
        data = data +rec
        print("received data:", rec)
        conn.send(bytes(data,'UTF-8'))  # echo
    point.fromString(data)
    conn.close()
    s.close()
    time.sleep(2)
    return data