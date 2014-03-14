'''
Created on 14.03.2014

@author: Thomas
'''
import threading
from Adafruit.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class LcdController(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.LCD = Adafruit_CharLCDPlate()
        self.LCD.clear()
        self.LCD.backlight(self.LCD.ON)
        self.LCD.message("Hexapod")
        self.running = True
        
    def run(self):
        while self.running:
            pass
    
    def Exit(self):
        self.LCD.backlight(self.LCD.OFF)
        self.running = False
        
    def push(self, data):
        self.LCD.clear()
        self.LCD.message(data)
    
    