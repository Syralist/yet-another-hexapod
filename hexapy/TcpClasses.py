'''
Created on 10.03.2014

@author: thomas
'''

import threading
import Queue
import socket

class TcpReceiver(threading.Thread):
    '''
    Implements the receiving part of a TCP connection.
    Forwards the received telegrams to a handler.
    '''
    def __init__(self, ip, port, socket, handler):
        '''
        Constructor. 
        Pass the connection info, the socket and the telegram handler.
        '''
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.BUFFER_SIZE = 64
        self.handler = handler
        print 'Receiver connected to:', self.ip, self.port
        
    def run(self):
        '''
        The run loop. 
        Read from socket and forward telegrams to the handler.
        '''
        print 'Receiver started...'
        while True:
            try:
                self.data = self.socket.recv(self.BUFFER_SIZE)
                if not self.data:
                    break
            except:
                print 'Connection closed!'
                break
            print "received data:", self.data
            self.handler.push(self.data)
            #self.socket.send(self.data)  # echo
        print 'Receiver exits...'
        #self.queue.join()
        self.handler.Exit()
        
class TcpSender(threading.Thread):
    '''
    Implements the sending part of a TCP connection.
    Uses a queue for safe threading.
    '''
    def __init__(self, ip, port, socket):
        '''
        Constructor. 
        Pass the connection info and the socket.
        '''
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.exit = False
        self.hasdata = False
        self.data = ''
        self.queue = Queue.Queue()
        print 'Sender connected to:', self.ip, self.port
        
    def run(self):
        '''
        The run loop. 
        Check for telegrams in the queue and send them.
        '''
        print 'Sender started...'
        while not self.exit:
            if not self.queue.empty():
                print 'things in the queue.'
                self.data = self.queue.get()
                self.socket.send(self.data)  # echo
                self.queue.task_done()
        print 'Sender exits...'
                
    def push(self, data):
        '''
        Put a telegram in the queue.
        '''
        self.queue.put(data)
        
    def Exit(self):
        '''
        Clean up the queue and exit.
        '''
        print 'Try to exit sender...'
        self.exit = True
        self.queue.join()
        
        
class TcpServer(threading.Thread):
    '''
    Implements a TCP server.
    Opens a socket, waits for a connection and starts the worker threads.
    '''
    def __init__(self, ip, port, handler=None):
        '''
        Constructor.
        Pass the connection info and an optional telegram handler.
        '''
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.handler = handler
        self.exit = False
        self.conn = None
    
    def run(self):
        '''
        The run loop.
        Open the socket, accept a connection, start the worker thread, then wait for the workers to end.
        '''
        #open and bind socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))
        self.socket.listen(1)
        while not self.exit:
            #wait for connection
            try:
                (self.conn, (self.distip, self.distport)) = self.socket.accept()
            except:
                continue
            
            self.MyTcpSender = TcpSender(self.distip, self.distport, self.conn)
            if self.handler == None:
                self.handler = self.MyTcpSender
            self.MyTcpReceiver = TcpReceiver(self.distip, self.distport, self.conn, self.handler)
            self.MyTcpReceiver.start()
            self.MyTcpSender.start()
            
            self.MyTcpSender.join()
            self.MyTcpReceiver.join()
        
    def Exit(self):
        '''
        Clean up and exit.
        '''
        print 'Try to exit server...'
        if not self.conn:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect( (self.ip, self.port))
        self.socket.close()
        self.MyTcpSender.Exit()
        self.exit = True
        
        
