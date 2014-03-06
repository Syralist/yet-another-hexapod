'''
Created on 24.02.2014

@author: thomas
'''

import socket
import threading
import Queue

class MyReceiver(threading.Thread):
    '''
    classdocs
    '''
    def __init__(self, ip, port, socket, sender):
        '''
        Constructor
        '''
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.BUFFER_SIZE = 20
        self.sender = sender
        print 'Receiver connected to:', self.ip, self.port
        
    def run(self):
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
            self.sender.push(self.data)
            #self.socket.send(self.data)  # echo
        print 'Receiver exits...'
        #self.queue.join()
        self.sender.Exit()
        
class MySender(threading.Thread):
    def __init__(self, ip, port, socket, queue):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        self.exit = False
        self.hasdata = False
        self.data = ''
        self.queue = queue
        print 'Sender connected to:', self.ip, self.port
        
    def run(self):
        print 'Sender started...'
        while not self.exit:
            if not self.queue.empty():
                print 'things in the queue.'
                self.data = self.queue.get()
                self.socket.send(self.data)  # echo
                self.queue.task_done()
        print 'Sender exits...'
                
    def push(self, data):
        self.queue.put(data)
        
    def Exit(self):
        print 'Try to exit sender...'
        self.exit = True
        self.queue.join()
    
if __name__ == "__main__":
    TCP_IP = '0.0.0.0'
    TCP_PORT = 55555
    MESSAGE = "Hello, World!"
    
    print MESSAGE
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    (conn, (ip, port)) = s.accept()
    
    newQueue = Queue.Queue()
    newSender = MySender(ip, port, conn, newQueue)
    newReceiver = MyReceiver(ip, port, conn, newSender)
    newReceiver.start()
    newSender.start()
    

