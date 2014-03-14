'''
Created on 24.02.2014

@author: thomas
'''

#import socket

from TcpClasses import TcpServer
from Adafruit/Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
    
if __name__ == "__main__":
    
    MESSAGE = "Hello, World!"
    print MESSAGE
    
    #bind to all addresses and listen on port 55555
    TCP_IP = '0.0.0.0'
    TCP_PORT = 55555
    
    MyTcpServer = TcpServer(TCP_IP, TCP_PORT)
    MyTcpServer.start()

    i = raw_input('Any key to exit...')
    
    MyTcpServer.Exit()