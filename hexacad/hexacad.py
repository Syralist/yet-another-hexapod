'''
Created on 17.03.2014

@author: Thomas
'''

import math
import numpy as np
import os

if __name__ == '__main__':
    
    points1 = []
    points2 = []
    
    maxdeg = 900
    lengthmm = 150
    widthmm = 90
    amplitudemm = 10
    
    forgnuplot = False
    
    
    for i in np.arange(0,maxdeg,1):
        points1.append([math.sin(float(i)/180*math.pi)*float(amplitudemm), float(lengthmm)/float(maxdeg)*float(i)])
    for i in np.arange(0,maxdeg,1):
        points2.append([math.sin(float(i)/180*math.pi)*float(amplitudemm)*-1.0 - float(widthmm), float(lengthmm)/float(maxdeg)*float(i)])
    
    points2.reverse()
            
    if forgnuplot:
        for [y, x] in points1:
            print x, " ", y 
        for [y, x] in points2:
            print x, " ", y
    else: 
        f = open("baseplate.scad", "w")
        f.write("module baseplate(){\n")
        f.write("linear_extrude(height=5)\n")
        f.write("polygon(" + str(points1 + points2) + ");\n")
        f.write("}\n")
        f.write("baseplate();")
        f.close()
