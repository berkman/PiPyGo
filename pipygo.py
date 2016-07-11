import cherrypy
# from cherrypy.process.plugins import Daemonizer
from classes.car import Car

my_car = Car()


class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

    # atexit.register(my_car.turn_off_motors())


class DriveWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        # TODO: do we want to use sessions?
        return cherrypy.session['motor_direction']

    def POST(self, motor_direction):
        cherrypy.session['motor_direction'] = motor_direction
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
