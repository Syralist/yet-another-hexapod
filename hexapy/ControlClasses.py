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
        self.Mover = MoveJoint(self.ServoHandler)
        self.Mover.start()
        
        self.Dummy = False
    
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
                    print self.Parts[1]
                    if self.Parts[1] == "set":
                        if self.Parts[2] in self.Servos:
                            try:
                                self.Mover.SetMovement(self.Parts[2], 
                                                       float(self.Parts[3]), 
                                                       float(self.Parts[4]), 
                                                       bool(self.Parts[5]), 
                                                       bool(self.Parts[6]))
                            except:
                                pass
                    elif self.Parts[1] == "init":
                        try:
                            self.Mover.InitMovement()
                        except:
                            pass
                    elif self.Parts[1] == "move":
                        try:
                            self.Mover.SetUpdate(True)
                        except:
                            pass
                    elif self.Parts[1] == "stop":
                        try:
                            self.Mover.SetUpdate(False)
                        except:
                            pass
            pass
    
    def Exit(self):
        self.Mover.Exit()
        self.Mover.join()
    
class MoveJoint(threading.Thread):
    def __init__(self, ServoHandler):
        threading.Thread.__init__(self)
        self.running = True
        self.doUpdate = False
        
        self.ServoHandler = ServoHandler
        self.Servos = self.ServoHandler.getJoints()
        self.MovementSetup = {k: [0.0, 0.0, False, False] for k in self.Servos} #Start, End, Repeat, Move
        self.MovementStatus = {k: [0.0, 0.0] for k in self.Servos} #Position, Direction
    
    def run(self):
        while self.running:
            if self.doUpdate:
                self.startTime = time.time()
                self.UpdateJoints()
                self.endTime = time.time()-self.startTime
                time.sleep(1.0-self.endTime)
        
    def Exit(self):
        self.running = False
        
    def SetUpdate(self, doUpdate):
        self.doUpdate = doUpdate
        
    def SetMovement(self, Joint, Start, End, Repeat, Move):
        if not self.doUpdate:
            try:
                self.MovementSetup[Joint][0] = Start
                self.MovementSetup[Joint][1] = End
                self.MovementSetup[Joint][2] = Repeat
                self.MovementSetup[Joint][3] = Move
            except:
                pass
    
    def InitMovement(self):
        if not self.doUpdate:
            for servo, movement in self.Servos, self.MovementSetup:
                print servo
                print movement
                if movement[3]:
                    self.MovementStatus[servo][0] = movement[0]
                    if movement[0] < movement[1]:
                        self.MovementStatus[servo][1] = 1.0
                    else:
                        self.MovementStatus[servo][1] = -1.0
                    self.ServoHandler.setAngle(servo, movement[0])
                
        
    def UpdateJoints(self):
        print self.startTime
        print self.MovementSetup
        print self.MovementStatus
