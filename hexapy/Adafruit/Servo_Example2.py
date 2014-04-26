#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 120                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

freq = 120
pwm.setPWMFreq(freq)                        # Set frequency to 60 Hz
cycle = 1.0/float(freq)
timepertick = cycle/4096
m = -0.0125
b = 1.5
ms = 0.0
a = 0.0
s = 0.0
ticks = 0
print timepertick

def AngleToPulse(angle):
  global a
  global m
  global b
  global ms
  global s
  global ticks
  global timepertick
  if a>40.0:
    a=40.0
  elif a<-40.0:
    a=-40.0
  print a
  ms = a*m+b
  if ms>2.0:
    ms=2.0
  elif ms<1.0:
    ms=1.0
  s = ms/1000
  print s
  ticks = int(s/timepertick)
  print ticks
  return ticks

pwm.setPWM(0, 0, AngleToPulse(0))
time.sleep(1)
pwm.setPWM(1, 0, AngleToPulse(0))
time.sleep(1)
pwm.setPWM(2, 0, AngleToPulse(0))
time.sleep(1)

while (True):
  # Change speed of continuous servo on channel O
  a = float(raw_input("Angle -40 to 40: "))
  pwm.setPWM(2, 0, AngleToPulse(a))
  #print 1
  #time.sleep(1)
  #setServoPulse(0, 50)
  #print 50
  #time.sleep(1)
  #setServoPulse(0, 100)
  #print 100
  #time.sleep(1)



