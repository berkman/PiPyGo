import cherrypy
# from cherrypy.process.plugins import Daemonizer
from classes.car import Car


class PiPyGo(object):
    my_car = Car()

    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def drive(self, drive_direction):
        self.my_car.set_drive_direction(drive_direction)
        return self.my_car.get_drive_direction()

    @cherrypy.expose
    @cherrypy.tools.allow(methods=['POST'])
    def steer(self, steering_direction):
        self.my_car.set_steering_direction(steering_direction)
        return self.my_car.get_steering_direction()

if __name__ == '__main__':
    config_file = "config/app2.conf"

    # d = Daemonizer(cherrypy.engine)
    # d.subscribe()

    cherrypy.quickstart(PiPyGo(), '/', config_file)
