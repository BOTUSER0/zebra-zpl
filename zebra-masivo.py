import socket
import os
from _thread import *
import re


f1 = open('shipping-iot-psk.zpl', 'r')
data = f1.read()


f = open('ipzebra.txt', 'r') #Text file with many ip address
o = f.read()
ip1 = re.findall( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", o )
hosts = ip1
ports = [9100]
for host in hosts:
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            print(result)
            if result == 0:
                    s.send(str.encode(data))
                    print (s.recv(1024)) #ACK
                    print("  [*] Port " + str(port) + " open!" + host)
            else: print("[+] CLOSE HOST " + host + ":" + str(port))
        except:
            pass
