#!/usr/bin/env python
import time
from car import Car
import atexit

my_car = Car()

my_car.set_drive_direction('FORWARD', drive_speed=50, drive_time=1)
print my_car.get_drive_direction()
my_car.set_drive_direction('FORWARD', drive_speed=250, drive_time=.1)
print my_car.get_drive_direction()
#my_car.set_drive_direction('NONE')
#print my_car.get_drive_direction()
