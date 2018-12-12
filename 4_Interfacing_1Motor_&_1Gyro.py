#!/usr/bin/env python3
# so that script can be run from Brickman

# If positive rotation is detected, then rotate motor in clockwise direction.
# If negative rotation is detected, then rotate motor in anti-clockwise direction.

from ev3dev.ev3 import *
from time import sleep

gy = GyroSensor(INPUT_4)                                   # Make object of GyroSensor class 
m = MediumMotor('outA')                                    # Make object of MediumMotor class
gy.mode='GYRO-ANG'                                         # Angle mode to receive only angular values

previous_value = 0;                                        # Variable necessary to count change in angle
while 1:
    current_value = gy.value()                             # Get instantaneous value of Gyro sensor
    if current_value != previous_value:                    # Only rotate motor only if change is detected
        if (current_value - previous_value) > 0:           # Check for positive rotation
            m.run_to_rel_pos(position_sp=(current_value - previous_value), speed_sp=400, stop_action="hold")
            print(str(current_value - previous_value))
            sleep(2)                                       # Give the motor time to move
        else:                                              # For negative rotation 
            m.run_to_rel_pos(position_sp=(current_value - previous_value), speed_sp=400, stop_action="hold")
            print(str(current_value - previous_value))
            sleep(2)                                       # Give the motor time to move
    previous_value = current_value                         # Update value for next iteration of loop

