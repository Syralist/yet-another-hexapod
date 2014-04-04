'''
Created on 17.03.2014

@author: Thomas
'''

import math
import numpy as np
import os

def plotbaseplate():
    points1 = []
    points2 = []
    
    mindeg = -90
    maxdeg = 990
    steps = abs(mindeg)+abs(maxdeg)
    lengthmm = 300
    widthmm = 180
    amplitudemm = 20
    
    forgnuplot = False
    
    
    for i in np.arange(mindeg,maxdeg,1):
        points1.append([math.sin(float(i)/180*math.pi)*float(amplitudemm), float(lengthmm)/float(steps)*float(i)])
    for i in np.arange(mindeg,maxdeg,1):
        points2.append([math.sin(float(i)/180*math.pi)*float(amplitudemm)*-1.0 - float(widthmm), float(lengthmm)/float(steps)*float(i)])
    
    points2.reverse()
            
    if forgnuplot:
        for [y, x] in points1:
            print x, " ", y 
        for [y, x] in points2:
            print x, " ", y
    else: 
        f = open("baseplate2.scad", "w")
        f.write("module baseplate(){\n")
        f.write("translate([0,25,0])\n")
        f.write("linear_extrude(height=5)\n")
        f.write("polygon(" + str(points1 + points2) + ");\n")
        f.write("}\n")
        f.write("baseplate();")
        f.close()
        
def plotfemur():
    points1 = []
    points2 = []
    
    mindeg = 0
    maxdeg = 180
    steps = abs(mindeg)+abs(maxdeg)
    lengthmm = 120
    widthmm = 40
    amplitudemm = 10
    
    forgnuplot = False
    
    
    for i in np.arange(mindeg,maxdeg,1):
        points1.append([math.sin(float(i)/180*math.pi)*float(amplitudemm), float(lengthmm)/float(steps)*float(i)])
    for i in np.arange(mindeg,maxdeg,1):
        points2.append([math.sin(float(i)/180*math.pi)*float(amplitudemm) - float(widthmm), float(lengthmm)/float(steps)*float(i)])
    
    points2.reverse()
            
    if forgnuplot:
        for [y, x] in points1:
            print x, " ", y 
        for [y, x] in points2:
            print x, " ", y
    else: 
        f = open("femur.scad", "w")
        f.write("module femurbase(){\n")
        f.write("translate([0,0,0])\n")
        f.write("linear_extrude(height=5)\n")
        f.write("polygon(" + str(points1 + points2) + ");\n")
        f.write("}\n")
        f.write("femurbase();")
        f.close()

if __name__ == '__main__':
    
    #plotbaseplate()
    plotfemur()
    pass
