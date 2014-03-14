'''
Created on 14.03.2014

@author: Thomas
'''
import threading
import time
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
        self.menu.Exit()
        self.menu.join()
        self.running = False
        
    def push(self, data):
        self.LCD.clear()
        self.data1 = data[:16]
        self.data2 = data[16:32]
        self.LCD.message(self.data1+"\n"+self.data2)
        
    def push2(self,data1,data2):
        self.LCD.clear()
        self.LCD.message(data1[:16]+"\n"+data2[:16])
    
class Menu(threading.Thread):
    def __init__(self, parent):
        self.mainmenulevel = 0
        self.submenu1level = 0
        
        self.mainmenuitem = 0
        self.submenu1item = 0
        
        self.mainmenu = ["Hexapod Mainmenu", "IP Adress"]
        
        self.parent = parent
        self.parent.push(self.mainmenu[self.mainmenuitem])
        
        self.running = True
        
    def run(self):
        while self.running:
            if self.mainmenulevel == 0 and self.mainmenuitem == 0:
                self.parent.push2(self.mainmenu[self.mainmenuitem],time.strftime("%H:%m:%s"))
        
    def Exit(self):
        self.running = False

    def up(self):
        pass
    
    def down(self):
        pass
    
    def left(self):
        pass
    
    def right(self):
        pass