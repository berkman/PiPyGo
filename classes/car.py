from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit
import time


class Car(object):
    steering_direction = None
    drive_direction = None
    drive_speed = None
    drive_time = None
    drive_motor = None
    steering_motor = None

    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT(addr=0x60)

    STEERING_DIRECTIONS = ['LEFT', 'RIGHT', 'RELEASE']
    DRIVE_DIRECTIONS = ['FORWARD', 'REVERSE', 'NONE']

    def __init__(self, steering_direction='RELEASE', drive_direction='NONE', drive_motor=mh.getMotor(1), steering_motor=mh.getMotor(2)):
        self.steering_direction = steering_direction
        self.drive_direction = drive_direction
        self.drive_motor = drive_motor
        self.steering_motor = steering_motor

    def get_steering_direction(self):
        return self.steering_direction

    def set_steering_direction(self, steering_direction):
        if steering_direction in self.STEERING_DIRECTIONS:
            self.steering_direction = steering_direction
        else:
            raise ValueError('Invalid Steering Direction')


    def get_drive_direction(self):
        return self.drive_direction

    def get_drive_speed(self):
        return self.drive_speed

    def get_drive_time(self):
        return self.drive_time

    def set_drive_direction(self, drive_direction, drive_speed=50, drive_time=0):
        if drive_direction == 'FORWARD':
            self.drive_direction = drive_direction
            self.drive_speed = drive_speed
            self.drive_time = drive_time
            self.drive_motor.run(Adafruit_MotorHAT.FORWARD)
            self.drive_motor.setSpeed(drive_speed)
            time.sleep(drive_time)
        elif drive_direction == 'REVERSE':
            self.drive_direction = drive_direction
            self.drive_speed = drive_speed
            self.drive_time = drive_time
            self.drive_motor.run(Adafruit_MotorHAT.BACKWARD)
            self.drive_motor.setSpeed(drive_speed)
            time.sleep(drive_time)
        elif drive_direction == 'NONE':
            self.drive_direction = drive_direction
            self.drive_speed = drive_speed
            self.drive_time = drive_time
            self.drive_motor.run(Adafruit_MotorHAT.RELEASE)
            self.drive_motor.setSpeed(drive_speed)
            time.sleep(drive_time)
        else:
            raise ValueError('Invalid Motor Direction')

    # recommended for auto-disabling motors on shutdown!
    def turn_off_motors(self):
        self.drive_motor.run(Adafruit_MotorHAT.RELEASE)
        self.steering_motor.run(Adafruit_MotorHAT.RELEASE)

    # atexit.register(turn_off_motors())
