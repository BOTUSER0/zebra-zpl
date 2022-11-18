import socket
import os
from _thread import *

print("Envio de configuracion shipping-iot.zpl")

def conn (printer):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    with open('shipping-iot.zpl', 'r') as f2:
        data = f2.read()
    port = 9100
    mysocket.connect((printer,port))
    while True:
        mysocket.send(str.encode(data))
        print(mysocket.recv(1024)) #recibe el ACK
        mysocket.close()

def printers ():
    file = open('ipzebra.txt', 'r')
    Lines = file.readlines()
    count = 0

    while True:  
        for line in Lines:
            count += 1
            if not line:
                count = 0
                break
        print(line.strip())
        printer = line.strip()
        
        return printer


conn(printers())
