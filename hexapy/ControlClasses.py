'''
Created on 07.06.2014

@author: Thomas
'''

class MessageHandler(object):
    '''
    classdocs
    '''


    def __init__(self, ServoHandler):
        '''
        Constructor
        '''
        self.ServoHandler = ServoHandler
    
    def push(self, data):
        self.ServoHandler.push(data)
    
    def Exit(self):
        pass