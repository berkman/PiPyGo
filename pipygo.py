import os, os.path
import string

from classes.car import Car

import cherrypy

my_car = Car()

class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class DriveWebService(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
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
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/drive': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/steer': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = PiPyGo()
    webapp.drive = DriveWebService()
    webapp.steer = SteerWebService()

    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(webapp, '/', conf)
