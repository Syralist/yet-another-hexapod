'''
Created on 22.03.2014

@author: Thomas
'''

import netifaces
import os

class SysInfo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.wlanip = "0.0.0.0"
        self.cpuload = "-"
        
    def updateIP(self):
        try:
            self.wlanip = netifaces.ifaddresses("wlan0")[2][0]['addr']
        except:
            self.wlanip = "0.0.0.0"
            
    def getIP(self):
        return self.wlanip
    
    def getCPUinfo(self):
        load = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
                                                                                       ))
        temp = str(os.popen('vcgencmd measure_temp').readline().replace("temp=","").strip(\
                                                                                       ))
        return(load + "% " + temp)
    
    