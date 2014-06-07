'''
Created on 22.03.2014

@author: Thomas
'''

from Adafruit.Adafruit_PWM_Servo_Driver import PWM

class ServoDriver(object):
    '''
    classdocs
    '''


    def __init__(self, address, channel, freq=60, maxangle=40.0, minangle=-40.0):
        '''
        Constructor
        '''
        self.channel = channel
        self.address = address
        self.freq = freq
        self.cycle = 1.0/float(self.freq)
        self.timepertick = self.cycle / 4096
        self.maxangle = maxangle
        self.minangle = minangle
        self.maxmilliseconds = 2.0
        self.minmilliseconds = 1.0
        self.m = (self.minmilliseconds - self.maxmilliseconds)/(self.maxangle - self.minangle)
        self.b = self.maxmilliseconds - (self.m * self.minangle)
        self.pwm = PWM()
        self.pwm.setPWMFreq(self.freq)
    
    def setAngle(self, angle):
        self.angle = angle
        print self.angle
        if self.angle > self.maxangle:
            self.angle = self.maxangle
        elif self.angle < self.minangle:
            self.angle = self.minangle
        self.milliseconds = self.angle * self.m + self.b
        print self.milliseconds
        if self.milliseconds > self.maxmilliseconds:
            self.milliseconds = self.maxmilliseconds
        elif self.milliseconds < self.minmilliseconds:
            self.milliseconds = self.minmilliseconds
        self.tickOn = (self.milliseconds/1000.0)/self.timepertick
        print self.tickOn
        self.pwm.setPWM(self.channel, 0, int(self.tickOn))
        
class ServoHandler(object):
    def __init__(self):
        self.Servos = {'CoxaL2': ServoDriver(0x40,0), 
                       'FemurL2': ServoDriver(0x40,1),
                       'TibiaL2': ServoDriver(0x40,2)}
        for servo in self.Servos:
            self.Servos[servo].setAngle(0)
        #self.Servos['FemurL2'].setAngle(0)
        #self.Servos['TibiaL2'].setAngle(0)
        
    def push(self, data):
        self.angle = 0.0
        self.joint = ""
        try:
            self.joint = data.split()[0]
            self.angle = float(data.split()[1])
            self.Servos[self.joint].setAngle(self.angle)
        except:
            pass
        
    def Exit(self):
        pass