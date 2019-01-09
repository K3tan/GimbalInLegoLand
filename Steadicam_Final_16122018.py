#!/usr/bin/env python3
# so that script can be run from Brickman

# Steadicam Final code 16/12/2018

from ev3dev.ev3 import *
from time import sleep
import os
# For better readability of output on EV3 display
os.system('setfont Lat15-TerminusBold14')                   

# Make object gy1 of GyroSensor class 
gy1 = GyroSensor(INPUT_3)                                   
# Make object gy2 of GyroSensor class
gy2 = GyroSensor(INPUT_4)  
# Make object m1 of MediumMotor class                                 
m1 = MediumMotor('outA')  
# Make object m2 of MediumMotor class
m2 = MediumMotor('outB')                                    

# Calibrate first gyroscope
gy1.mode='GYRO-CAL'                                         
# Calibrate second gyroscope
gy2.mode='GYRO-CAL'                                         
sleep(1)
# Indicate that EV3 is ready
Sound.beep()
# Angle mode to receive only angular values
gy1.mode='GYRO-ANG'                                         
gy2.mode='GYRO-ANG'                                         

while 1:
    # Get instantaneous value of orientation of first plane
    gy1_current_value = gy1.value()                         

    # Define tolerance of +/-2°
    if (2 < gy1_current_value) or (gy1_current_value < -2): 
        # Check for clockwise rotation of motor 1
        if gy1_current_value > 0:                           
            m1.run_to_rel_pos(position_sp=-gy1_current_value, speed_sp=300, stop_action="brake")
            print('Rotation = ',str(gy1_current_value))
            # Give the motor time to move
            sleep(1.5)                                        
        # Check for anti-clockwise rotation of motor 1    
        else:                                               
            m1.run_to_rel_pos(position_sp=-(0.8 * gy1_current_value), speed_sp=300, stop_action="brake")
            print('Rotation = ',str(gy1_current_value))
            # Give the motor time to move 
            sleep(1.5)                                        
                                                 
    # Get instantaneous value of orientation of second plane
    gy2_current_value = gy2.value()                         

    # Define tolerance of +/-2°
    if (2 < gy2_current_value) or (gy2_current_value < -2):     
        # Check for clockwise rotation of motor 2
        if gy2_current_value > 0:                           
            m2.run_to_rel_pos(position_sp=-gy2_current_value, speed_sp=300, stop_action="brake")
            print('Rotation = ',str(gy2_current_value))
            # Give the motor time to move
            sleep(1.5)                             
        # Check for anti-clockwise rotation of motor 2
        else:                                               
            m2.run_to_rel_pos(position_sp=-(0.8 * gy2_current_value), speed_sp=300, stop_action="brake")
            print('Rotation = ',str(gy2_current_value))
            # Give the motor time to move  
            sleep(1.5)                                        
    
    # Sleep time to ensure for the vibrations after motor movements have gone                                                
    sleep(0.5)
    

