'''
Created on 07.06.2014

@author: Thomas
'''
import threading
import time

class MessageHandler(object):
    '''
    classdocs
    '''


    def __init__(self, ServoHandler):
        '''
        Constructor
        '''
        self.ServoHandler = ServoHandler
        self.Mover = MoveJoint()
        self.Mover.start()
    
    def push(self, data):
        self.DirectPush = False
        if self.DirectPush:
            self.ServoHandler.push(data)
        else:
            self.Messages = data.split(';')
            self.Servos = self.ServoHandler.getJoints()
            self.Joint = ""
            self.Angle = 0.0
            self.Message = ""
            self.Dummy = False
            for Message in self.Messages:
                self.Parts = Message.split()
                if self.Parts[0] == "setJoint":
                    if self.Parts[1] in self.Servos:
                        try:
                            self.Joint = self.Parts[1]
                            self.Angle = float(self.Parts[2])
                            self.ServoHandler.setAngle(self.Joint, self.Angle)
                        except:
                            pass
                        self.Angle = 0.0
                        self.Joint = ""
                elif self.Parts[0] == "moveJoint":
                    self.Dummy = not self.Dummy
                    self.Mover.SetUpdate(self.Dummy)
            pass
    
    def Exit(self):
        self.Mover.Exit()
        self.Mover.join()
    
class MoveJoint(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.doUpdate = False
    
    def run(self):
        while self.running:
            if self.doUpdate:
                self.startTime = time.time()
                self.UpdateJoints()
                self.endTime = time.time()-self.startTime
                time.sleep(0.1-self.endTime)
        
    def Exit(self):
        self.running = False
        
    def SetUpdate(self, doUpdate):
        self.doUpdate = doUpdate
        
    def UpdateJoints(self):
        print self.startTime
