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
        self.DirectPush = True
        if self.DirectPush:
            self.ServoHandler.push(data)
        else:
            self.MessageParts = data.split()
            self.Servos = self.ServoHandler.getJoints()
            self.Joint = ""
            self.Angle = 0.0
            for Part in self.Messageparts:
                if Part in self.Servos:
                    self.Joint = Part
                elif self.Joint != "":
                    self.Angle = float(Part)
                    try:
                        self.ServoHandler.setAngle(self.Joint, self.Angle)
                    except:
                        pass
                    self.Angle = 0.0
                    self.Joint = ""
            pass
    
    def Exit(self):
        pass