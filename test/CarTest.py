#!/usr/bin/env python

from classes.car import Car

my_car = Car()

my_car.set_motor_direction('FORWARD')
my_car.set_steering_direction('CENTER')

print my_car.get_motor_direction()
print my_car.get_steering_direction()
