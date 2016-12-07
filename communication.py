#file for two party communication
#Simply uses sockets to create tcp connection to given ip address and port

import socket
import time


def sendInfo(stringToSend,tcp_ip,tcp_port):
    print("Sending")
    BUFFER_SIZE = 1024
    #open socket to send data
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    s.send(bytes(stringToSend,'UTF-8'))
    #then open recieve so we don't keep sending junk and confirm they
    #received our data
    data = s.recv(BUFFER_SIZE)
    s.close()
    
def recInfo(point,myIpAddress,myPort):
    print("Recieving")
    BUFFER_SIZE = 1024
    #open socket and set it to listen for communication
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((myIpAddress, myPort))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)
    data = ""
    while 1:
        #keep running till we receive data
        rec = conn.recv(BUFFER_SIZE).decode('UTF-8')
        if not rec: break
        data = data +rec
        print("received data:", rec)
        # echo data back so they can confirm we received
        conn.send(bytes(data,'UTF-8'))
    #print what we recieved and close connection
    point.fromString(data)
    conn.close()
    s.close()
    time.sleep(2)
    return data