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

    mh = Adafruit_MotorHAT()


    def __init__(self, steering_direction='RELEASE', drive_direction='NONE',
        drive_motor=mh.getMotor(1), steering_motor=mh.getMotor(2)):

        self.steering_direction = steering_direction
        self.drive_direction = drive_direction
        self.drive_motor = drive_motor
        self.steering_motor = steering_motor

        atexit.register(self.turn_off_motors)

    def get_steering_direction(self):
        return self.steering_direction

    def set_steering_direction(self, steering_direction):
        pass

    def get_drive_direction(self):
        return self.drive_direction

    def get_drive_speed(self):
        return self.drive_speed

    def get_drive_time(self):
        return self.drive_time

    def set_drive_direction(self, drive_direction, drive_speed=50, drive_time=0):
        self.drive_direction = drive_direction
        self.drive_speed = drive_speed
        self.drive_time = drive_time
        self.drive_motor.setSpeed(drive_speed)

        if drive_direction == 'FORWARD':
            self.drive_motor.run(Adafruit_MotorHAT.FORWARD)
        elif drive_direction == 'REVERSE':
            self.drive_motor.run(Adafruit_MotorHAT.BACKWARD)
        else:
            self.drive_motor.run(Adafruit_MotorHAT.RELEASE)

        time.sleep(drive_time)

    def turn_off_motors(self):
        self.drive_motor.run(Adafruit_MotorHAT.RELEASE)
        self.steering_motor.run(Adafruit_MotorHAT.RELEASE)
