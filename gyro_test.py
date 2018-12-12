#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

# Connect gyro and touch sensors to any sensor ports
gy = GyroSensor(INPUT_2) 

# Put the gyro sensor into ANGLE mode.
gy.mode='GYRO-ANG'

units = gy.units
#reports 'deg' meaning degrees

while 1:    
    angle = gy.value()
    print(str(angle))
    sleep(0.5)