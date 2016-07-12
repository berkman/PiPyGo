import cherrypy
# from cherrypy.process.plugins import Daemonizer
from classes.car import Car
import atexit


class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')


class DriveWebService(object):
    exposed = True

    my_car = Car()

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return my_car.get_drive_direction

    def POST(self, drive_direction):
        self.my_car.set_drive_direction(drive_direction)
        return drive_direction


class SteerWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        pass
        # my_car.get_steering_direction

    def POST(self, steering_direction):
        # self.my_car.set_steering_direction(steering_direction)
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
