import cherrypy
from cherrypy.process.plugins import Daemonizer
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
from classes.car import Car

my_car = Car()

# TODO move to car class?
# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
myMotor = mh.getMotor(3)


class PiPyGo(object):
    @cherrypy.expose

    # TODO move to car class?
    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    atexit.register(turnOffMotors)

    def index(self):
        return open('/Users/mberkman/index.html')

class DriveWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['motor_direction']

    def POST(self, motor_direction):
        cherrypy.session['motor_direction'] = motor_direction

        # TODO move to car class?
        # print "Forward!"
        # myMotor.run(Adafruit_MotorHAT.FORWARD)
        # myMotor.setSpeed(255)

        # print "Backward!"
        # myMotor.run(Adafruit_MotorHAT.BACKWARD)
        # myMotor.setSpeed(255)

        # print "Release"
        # myMotor.run(Adafruit_MotorHAT.RELEASE)

        # self.my_car.set_motor_direction = motor_direction
        return motor_direction

class SteerWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['steering_direction']

    def POST(self, steering_direction):
        cherrypy.session['steering_direction'] = steering_direction
        # self.my_car.set_steering_direction = steering_direction
        return steering_direction

if __name__ == '__main__':
    config_file = "config/app.conf"
    cherrypy.log("Config File: %s" % config_file)

    # d = Daemonizer(cherrypy.engine)
    # d.subscribe()

    webapp = PiPyGo()
    webapp.drive = DriveWebService()
    webapp.steer = SteerWebService()

    cherrypy.quickstart(webapp, '/', config_file)