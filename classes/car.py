from Adafruit_MotorHAT import Adafruit_MotorHAT
import atexit


class Car(object):
    steering_direction = None
    motor_direction = None

    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT(addr=0x60)
    myDriveMotor = mh.getMotor(3)
    mySteerMotor = mh.getMotor(4)

    STEERING_DIRECTIONS = ['LEFT', 'RIGHT', 'NONE']
    MOTOR_DIRECTIONS = ['FORWARD', 'REVERSE', 'NONE']

    def __init__(self, steering_direction='NONE', motor_direction='NONE'):
        self.steering_direction = steering_direction
        self.motor_direction = motor_direction

    def get_steering_direction(self):
        return self.steering_direction

    def get_motor_direction(self):
        return self.motor_direction

    def set_steering_direction(self, steering_direction):
        if steering_direction in self.STEERING_DIRECTIONS:
            self.steering_direction = steering_direction
        else:
            raise ValueError('Invalid Steering Direction')

    def set_motor_direction(self, motor_direction):
        if motor_direction in self.MOTOR_DIRECTIONS:
            self.motor_direction = motor_direction
        else:
            raise ValueError('Invalid Motor Direction')

        # myDriveMotor.run(Adafruit_MotorHAT.FORWARD)
        # myDriveMotor.setSpeed(255)
        # myDriveMotor.run(Adafruit_MotorHAT.BACKWARD)
        # myDriveMotor.run(Adafruit_MotorHAT.RELEASE)

    # recommended for auto-disabling motors on shutdown!
    def turn_off_motors():
        self.myDriveMotor.run(Adafruit_MotorHAT.RELEASE)
        self.mySteerMotor.run(Adafruit_MotorHAT.RELEASE)

    atexit.register(turn_off_motors)
