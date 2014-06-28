'''
Created on 07.06.2014

@author: Thomas
'''
import threading
import time

import TcpClasses

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
        
        self.ForwardHandler = None
        
    def setForwardHandler(self, ForwardHandler):
        self.ForwardHandler = ForwardHandler
    
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
                if len(self.Parts) < 2:
                    if self.ForwardHandler != None:
                        self.ForwardHandler.push("Message '"+str(self.Parts)+"' malformed\n")
                    continue
                if self.Parts[0] == "setJoint":
                    if self.Parts[1] in self.Servos:
                        try:
                            self.Joint = self.Parts[1]
                            self.Angle = float(self.Parts[2])
                            self.ServoHandler.setAngle(self.Joint, self.Angle)
                            if self.ForwardHandler != None:
                                self.ForwardHandler.push("Joint "+self.Joint+" set to "+str(self.Angle)+"\n")
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
                                if self.ForwardHandler != None:
                                    self.ForwardHandler.push("Set joint movement for "+self.Parts[2]+" as "+self.Parts[3]+" to "+self.Parts[4]+"\n")
                            except:
                                pass
                    elif self.Parts[1] == "init":
                        try:
                            self.Mover.InitMovement()
                            if self.ForwardHandler != None:
                                self.ForwardHandler.push("Joint movement initialized\n")
                        except:
                            pass
                    elif self.Parts[1] == "move":
                        try:
                            self.Mover.SetUpdate(True)
                            if self.ForwardHandler != None:
                                self.ForwardHandler.push("Joint movement started\n")
                        except:
                            pass
                    elif self.Parts[1] == "stop":
                        try:
                            self.Mover.SetUpdate(False)
                            if self.ForwardHandler != None:
                                self.ForwardHandler.push("Joint movement stopped\n")
                        except:
                            pass
                else:
                    if self.ForwardHandler != None:
                        self.ForwardHandler.push("Message '"+str(self.Parts)+"' incomprehensible\n")
    
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
                self.elapsedTime = time.time()-self.startTime
                self.sleepTime = 0.10-self.elapsedTime
                print self.elapsedTime
                if self.sleepTime < 0.0:
                    self.sleepTime = 0.0
                time.sleep(self.sleepTime)
        
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
            for servo, movement in self.MovementSetup.iteritems():
                print servo
                print movement
                if movement[3]:
                    self.MovementStatus[servo][0] = movement[0]
                    # set increment
                    self.MovementStatus[servo][1] = 1.0
                    if movement[0] < movement[1]:
                        self.MovementStatus[servo][1] *= 1.0
                    else:
                        self.MovementStatus[servo][1] *= -1.0
                    self.ServoHandler.setAngle(servo, movement[0])
                
        
    def UpdateJoints(self):
        #print self.startTime
        #print self.MovementSetup #Start, End, Repeat, Move
        #print self.MovementStatus #Position, Direction/Increment
        for servo in self.Servos:
            #print servo
            if self.MovementSetup[servo][3]:
                #print 'Move = True'
                self.MovementStatus[servo][0] += self.MovementStatus[servo][1]
                self.ServoHandler.setAngle(servo,self.MovementStatus[servo][0])
                if (self.MovementSetup[servo][0] < self.MovementSetup[servo][1]):
                    #print 'Start < End'
                    if (((self.MovementStatus[servo][0] >= self.MovementSetup[servo][1]) 
                        or
                        (self.MovementStatus[servo][0] <= self.MovementSetup[servo][0]))
                        and self.MovementSetup[servo][2]):
                        #print 'Position >= End && Repeat'
                        #print '#Position <= Start && Repeat'
                        self.MovementStatus[servo][1] *= -1.0
                else:
                    #print 'Start > End'
                    if (((self.MovementStatus[servo][0] >= self.MovementSetup[servo][0]) 
                        or
                        (self.MovementStatus[servo][0] <= self.MovementSetup[servo][1]))
                        and self.MovementSetup[servo][2]):
                        #print 'Position >= End && Repeat'
                        #print 'Position <= Start && Repeat'
                        self.MovementStatus[servo][1] *= -1.0
