'''
Created on 24.02.2014

@author: thomas
'''

import socket

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
if __name__ == "__main__":
    TCP_IP = '0.0.0.0'
    TCP_PORT = 55555
    BUFFER_SIZE = 20
    MESSAGE = "Hello, World!"
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data:", data
        conn.send(data)  # echo
    conn.close()
