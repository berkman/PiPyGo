#!/usr/bin/env python

from Car import Car


my_car = Car()

my_car.set_motor_speed('HIGH')
my_car.set_steering_direction('CENTER')

print my_car.get_motor_speed()
print my_car.get_steering_direction()

print my_car.get_pedal_engaged()
print my_car.get_steering_engaged()
