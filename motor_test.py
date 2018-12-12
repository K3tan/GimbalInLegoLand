#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.ev3 import *
from time import sleep

m = MediumMotor('outA')

while 1:
    m.run_to_rel_pos(position_sp=180, speed_sp=400, stop_action="hold")
    sleep(5)   # Give the motor time to move
    m.run_to_rel_pos(position_sp=-180, speed_sp=400, stop_action="hold")
    sleep(5)   # Give the motor time to move