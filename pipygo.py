import os, os.path
import string

from classes.car import Car

import cherrypy

class PiPyGo(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

class PiPyGoWebService(object):
    exposed = True
    my_car = Car()

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return cherrypy.session['motor_direction']

    def POST(self, motor_direction):
        cherrypy.session['motor_direction'] = motor_direction
        self.my_car.set_motor_direction = motor_direction

        return motor_direction

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/command': {
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
    webapp.command = PiPyGoWebService()
    cherrypy.quickstart(webapp, '/', conf)

    #cherrypy.engine.start()
    #cherrypy.engine.block()
