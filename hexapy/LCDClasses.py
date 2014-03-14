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
        threading.Thread.__init__(self)
        self.LCD = Adafruit_CharLCDPlate()
        self.LCD.clear()
        self.LCD.backlight(self.LCD.ON)
        self.LCD.message("Hexapod")
        self.running = True
        
        self.menu = Menu(self)
        
    def run(self):
        while self.running:
            pass
    
    def Exit(self):
        self.LCD.backlight(self.LCD.OFF)
        self.running = False
        
    def push(self, data):
        self.LCD.clear()
        self.data1 = data[:16]
        self.data2 = data[16:32]
        self.LCD.message(self.data1+"\n"+self.data2)
    
class Menu(object):
    def __init__(self, parent):
        self.mainmenulevel = 0
        self.submenu1level = 0
        
        self.mainmenuitem = 0
        self.submenu1item = 0
        
        self.mainmenu = ["Hexapod"]
        
        self.parent = parent
        
        self.parent.push(self.mainmenu[self.mainmenuitem])
