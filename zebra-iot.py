import socket
import os
from _thread import *

salir=False

while not salir:
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Envio de configuracion Shipping-iot")
    with open('shipping-iot-psk.zpl', 'r') as f2:
        data = f2.read()
        print(data)
    printer=str(input("Ingrese IP de impresora:"))
    if printer == 'end':
        salir = True
    else:
        port = 9100
        mysocket.connect((printer,port))
        mysocket.send(str.encode(data))
        print(mysocket.recv(1024)) #recibe el ACK
        mysocket.close()
