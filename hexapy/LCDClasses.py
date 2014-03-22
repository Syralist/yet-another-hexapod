'''
Created on 14.03.2014

@author: Thomas
'''
import threading
import time

from Adafruit.Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from SysInfo import SysInfo

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
        self.menu.start()
        
        
    def run(self):
        while self.running:
            if self.LCD.buttonPressed(self.LCD.LEFT):
                self.menu.left()
            if self.LCD.buttonPressed(self.LCD.RIGHT):
                self.menu.right()
            if self.LCD.buttonPressed(self.LCD.UP):
                self.menu.up()
            if self.LCD.buttonPressed(self.LCD.DOWN):
                self.menu.down()
            if self.LCD.buttonPressed(self.LCD.SELECT):
                self.menu.select()
    
    def Exit(self):
        self.LCD.backlight(self.LCD.OFF)
        self.LCD.clear()
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
        threading.Thread.__init__(self)
        self.menuitem = 0
        
        self.menu = ["Hexapod Mainmenu", "IP Adress", "CPU Load"]
        
        self.parent = parent
        self.parent.push(self.menu[self.menuitem])
        
        self.running = True
        self.timestamp = int(time.time())
        self.timechanged = False
        
        self.sysinfo = SysInfo()
        self.sysinfo.updateIP()
        
    def run(self):
        while self.running:
            if int(time.time()) > self.timestamp:
                self.timestamp = int(time.time())
                self.timechanged = True
            else:
                self.timechanged = False
                
            if self.timechanged:
                if self.menuitem == 0:
                    self.parent.push2(self.menu[self.menuitem],time.strftime("%H:%M:%S"))
                elif self.menuitem == 1:
                    self.parent.push2(self.menu[self.menuitem],self.sysinfo.getIP())
                elif self.menuitem == 2:
                    self.parent.push2(self.menu[self.menuitem],self.sysinfo.getCPUuse())
        
    def Exit(self):
        self.running = False

    def up(self):
        self.menuitem -= 1
        if self.menuitem < 0:
            self.menuitem = len(self.menu)-1
    
    def down(self):
        self.menuitem += 1
        if self.menuitem > len(self.menu)-1:
            self.menuitem = 0
    
    def left(self):
        pass
    
    def right(self):
        pass
    
    def select(self):
        pass
