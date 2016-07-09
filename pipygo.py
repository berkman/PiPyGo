import json
import uuid
import os

from classes.car import Car

import cherrypy
from cherrypy.process.plugins import Daemonizer

my_car = Car()

class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class DriveWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    #@cherrypy.tools.json_out()
    def GET(self):
        '''
        response = {
            'request_tag':  str(uuid.uuid1()),
            'one':          'one',
            'two':          'two'
        }

        response = json.dumps(response)
        cherrypy.log(response)
        '''
        return cherrypy.session['motor_direction']

    def POST(self, motor_direction):
        cherrypy.session['motor_direction'] = motor_direction
        #self.my_car.set_motor_direction = motor_direction
        return motor_direction

class SteerWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['steering_direction']

    def POST(self, steering_direction):
        cherrypy.session['steering_direction'] = steering_direction
        #self.my_car.set_steering_direction = steering_direction
        return steering_direction

if __name__ == '__main__':
    config_file = "/apps/config/app.conf"
    cherrypy.log("Config File: %s" % config_file)

    d = Daemonizer(cherrypy.engine)
    d.subscribe()

    webapp = PiPyGo()
    webapp.drive = DriveWebService()
    webapp.steer = SteerWebService()

    cherrypy.quickstart(webapp, '/', config_file)
